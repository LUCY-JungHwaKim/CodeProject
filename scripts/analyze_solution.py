#!/usr/bin/env python3
"""
push된 풀이 코드를 분석해서 티스토리에 올릴 블로그 글 초안(.md)을
자동 생성하는 스크립트.

v2: 백준(BOJ) + 프로그래머스(Programmers) 둘 다 지원.
    (2026.04.28 BOJ 서비스 종료 이후 프로그래머스 지원 추가)

- LLM을 쓰지 않는 "템플릿 + 정규식 기반" 분석기입니다.
- 문제 번호/플랫폼은 아래 순서로 찾습니다 (우선순위 순):
    1) 코드 안에 문제 URL이 그대로 있는 경우 (가장 정확)
       예: https://school.programmers.co.kr/learn/courses/30/lessons/12909
       예: https://www.acmicpc.net/problem/1926
    2) 코드 상단 주석에 "백준"/"BOJ" 또는 "프로그래머스"/"programmers" + 숫자가 있는 경우
       예: # 프로그래머스 12909, // BOJ 1926
    3) 파일명이 숫자인 경우 (예: 1926.py) — 이 경우 플랫폼을 확정할 수 없어 'unknown' 처리
- 문제 제목은 각 플랫폼 사이트에서 크롤링합니다 (실패 시 "{번호}번 문제"로 대체).
- 사용된 알고리즘 패턴은 정규식으로 "추정"만 합니다. 실제 풀이 설명(접근 방법/회고)은
  사람이 직접 채우도록 TODO로 남겨둡니다.

사용법:
    python scripts/analyze_solution.py changed_files.txt
"""

import os
import re
import sys
from datetime import datetime, timezone

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    requests = None
    BeautifulSoup = None


EXT_LANG = {
    ".py": "python",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".c": "c",
    ".java": "java",
    ".js": "javascript",
    ".ts": "typescript",
    ".kt": "kotlin",
    ".go": "go",
    ".rs": "rust",
}

PLATFORMS = {
    "baekjoon": {
        "label": "백준",
        "url_template": "https://www.acmicpc.net/problem/{num}",
    },
    "programmers": {
        "label": "프로그래머스",
        "url_template": "https://school.programmers.co.kr/learn/courses/30/lessons/{num}",
    },
    "unknown": {
        "label": "미확인 플랫폼",
        "url_template": None,
    },
}

# (태그, 정규식, 사람이 읽을 설명 문장)
PATTERNS = [
    ("BFS", r"\b(bfs|deque|Queue\(\))\b", "BFS(너비 우선 탐색)를 활용하는 것으로 보입니다."),
    ("DFS", r"\b(dfs|visited)\b", "DFS(깊이 우선 탐색) 혹은 방문 배열을 활용하는 탐색 문제로 보입니다."),
    ("DP", r"\b(dp\s*\[|memo)\b", "다이나믹 프로그래밍(DP) 기법을 사용한 것으로 보입니다."),
    ("정렬", r"\b(sort|sorted|Arrays\.sort)\b", "정렬을 활용하는 문제로 보입니다."),
    ("이분탐색", r"\b(bisect|lower_bound|upper_bound)\b|\bmid\s*=", "이분 탐색(Binary Search)을 사용한 것으로 보입니다."),
    ("우선순위큐", r"\b(heapq|PriorityQueue|priority_queue)\b", "우선순위 큐(힙)를 활용한 것으로 보입니다."),
    ("유니온파인드", r"\b(find_parent|union\(|parent\[)\b", "유니온 파인드(Union-Find) 구조를 사용한 것으로 보입니다."),
    ("백트래킹", r"\b(backtrack|permutations|combinations)\b", "백트래킹/완전탐색 기법을 사용한 것으로 보입니다."),
    ("그래프", r"\b(graph\[|adj\[|adjacency)\b", "그래프 자료구조를 활용하는 문제로 보입니다."),
    ("투포인터", r"\b(left|start)\b[\s\S]{0,60}\b(right|end)\b", "투 포인터(Two Pointer) 기법을 사용했을 가능성이 있습니다."),
    ("스택/큐", r"\b(stack|deque|append\(.+\)\s*\n.+pop)\b", "스택 또는 큐 자료구조를 활용하는 것으로 보입니다."),
]


def detect_platform_and_number(filepath: str, content: str):
    """(platform_key, number) 튜플을 반환. 못 찾으면 (None, None)."""

    # 1) 코드 안에 문제 URL이 그대로 있는 경우 - 가장 신뢰도 높음
    m = re.search(r"programmers\.co\.kr/learn/courses/30/lessons/(\d+)", content)
    if m:
        return "programmers", m.group(1)

    m = re.search(r"acmicpc\.net/problem/(\d+)", content)
    if m:
        return "baekjoon", m.group(1)

    # 2) 코드 상단 15줄 안의 주석 키워드 + 숫자
    header = "\n".join(content.splitlines()[:15])

    m = re.search(r"(?:프로그래머스|programmers)\D{0,10}(\d{3,7})", header, re.IGNORECASE)
    if m:
        return "programmers", m.group(1)

    m = re.search(r"(?:백준|BOJ|boj)\D{0,10}(\d{3,7})", header, re.IGNORECASE)
    if m:
        return "baekjoon", m.group(1)

    # 3) 파일명이 숫자인 경우 - 플랫폼은 알 수 없음
    stem = os.path.splitext(os.path.basename(filepath))[0]
    if re.fullmatch(r"\d{3,7}", stem):
        return "unknown", stem

    m = re.search(r"(\d{3,7})", stem)
    if m:
        return "unknown", m.group(1)

    return None, None


def fetch_problem_title(platform: str, number: str):
    if requests is None or BeautifulSoup is None:
        return None

    headers = {"User-Agent": "Mozilla/5.0 (compatible; blog-draft-bot)"}

    try:
        if platform == "baekjoon":
            resp = requests.get(
                f"https://www.acmicpc.net/problem/{number}", timeout=5, headers=headers
            )
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            title_tag = soup.select_one("#problem_title")
            if title_tag:
                return title_tag.get_text(strip=True)

        elif platform == "programmers":
            resp = requests.get(
                f"https://school.programmers.co.kr/learn/courses/30/lessons/{number}",
                timeout=5,
                headers=headers,
            )
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            if soup.title and soup.title.string:
                # <title>코딩테스트 연습 - 올바른 괄호 | 프로그래머스 스쿨</title>
                raw = soup.title.string.strip()
                m = re.search(r"-\s*(.+?)\s*\|", raw)
                if m:
                    return m.group(1).strip()
                return raw

    except Exception as e:  # noqa: BLE001
        print(f"[WARN] {platform} {number}번 문제 제목을 가져오지 못했습니다: {e}")

    return None


def detect_patterns(content: str):
    found = []
    for name, pattern, desc in PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            found.append((name, desc))
    return found[:5]  # 너무 많이 잡히면 노이즈이므로 상위 5개만


def build_markdown(platform, number, title, language, code, tags, source_path):
    platform_info = PLATFORMS.get(platform, PLATFORMS["unknown"])
    platform_label = platform_info["label"]
    url = platform_info["url_template"].format(num=number) if platform_info["url_template"] else None

    tag_names = ", ".join(t[0] for t in tags) if tags else "미분류"
    tag_bullets = (
        "\n".join(f"- {desc}" for _, desc in tags)
        if tags
        else "- 자동으로 감지된 패턴이 없습니다. 직접 유형을 적어주세요."
    )
    today = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")

    link_line = f"- 문제 링크: {url}" if url else (
        "- 문제 링크: **TODO** (플랫폼을 자동으로 판별하지 못했습니다. "
        "파일 상단에 `# 프로그래머스 12909` 또는 `# 백준 1926` 형식의 주석을 추가하면 "
        "다음 push부터 자동으로 채워집니다.)"
    )
    platform_note = "" if platform != "unknown" else "\n> ⚠️ 이 문제의 출처 플랫폼을 자동으로 판별하지 못했습니다. 위 TODO를 참고해 코드에 주석을 추가해주세요.\n"

    return f"""# [{platform_label} {number}] {title} 풀이

{link_line}
- 사용 언어: {language}
- 예상 유형(자동 감지): {tag_names}
- 원본 코드: `{source_path}`
- 생성일: {today}
{platform_note}
## 문제 설명

> {title}
>
> (자세한 문제 설명 및 제약 조건은 위 링크를 참고해주세요.)

## 접근 방법

아래는 코드 패턴을 정규식으로 훑어 **추정**한 알고리즘 유형입니다.
실제 풀이 논리와 다를 수 있으니 확인 후 자연어로 다듬어서 채워주세요.

{tag_bullets}

**TODO:** 문제를 어떻게 접근했는지, 핵심 아이디어와 시행착오를 여기에 직접 적어주세요.
(예: 처음에 어떤 방법을 시도했다가 왜 실패했는지, 최종적으로 어떤 아이디어로 풀었는지)

## 코드

```{language}
{code}
```

## 시간복잡도

**TODO:** 시간/공간 복잡도를 적어주세요.

## 회고

**TODO:** 풀면서 배운 점, 실수했던 부분, 다음에 비슷한 문제를 만나면 어떻게 할지 적어주세요.

---
*이 글은 push 시 자동으로 생성된 초안입니다. 티스토리에 올리기 전에 위 TODO 항목들을 채우고 자유롭게 다듬어주세요.*
"""


def main():
    if len(sys.argv) < 2:
        print("사용법: python analyze_solution.py <changed_files.txt>")
        sys.exit(1)

    changed_files_path = sys.argv[1]
    with open(changed_files_path, encoding="utf-8") as f:
        files = [line.strip() for line in f if line.strip()]

    os.makedirs("blog-drafts", exist_ok=True)

    generated = []

    for filepath in files:
        if filepath.startswith("blog-drafts/"):
            continue
        if not os.path.exists(filepath):
            continue  # 삭제된 파일

        ext = os.path.splitext(filepath)[1]
        if ext not in EXT_LANG:
            continue

        with open(filepath, encoding="utf-8", errors="ignore") as f:
            content = f.read()

        platform, number = detect_platform_and_number(filepath, content)
        if not number:
            print(f"[SKIP] {filepath}: 문제 번호를 찾을 수 없습니다.")
            continue

        language = EXT_LANG[ext]
        title = fetch_problem_title(platform, number) or f"{number}번 문제"
        tags = detect_patterns(content)

        md = build_markdown(platform, number, title, language, content, tags, filepath)

        out_path = f"blog-drafts/{platform}-{number}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        generated.append(out_path)
        print(f"[OK] {out_path} 생성됨 ({platform} {number}: {title})")

    if not generated:
        print("생성된 초안이 없습니다. (문제 번호를 인식할 수 있는 파일이 push되지 않음)")


if __name__ == "__main__":
    main()
