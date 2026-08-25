#!/usr/bin/env python3

"""
Push된 코딩테스트 풀이 코드를 분석하여
티스토리에 올릴 Markdown 블로그 초안을 자동 생성합니다.

지원 플랫폼
- 프로그래머스
- 백준

동작 과정
1. push된 파일 목록 확인
2. 문제 플랫폼 / 번호 감지
3. 문제 제목 가져오기
4. OpenAI API로 실제 풀이 코드 분석
5. 접근 방법 / 시간복잡도 / 회고 작성
6. blog-drafts/*.md 생성
"""

import os
import re
import sys
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup
from openai import OpenAI


# --------------------------------------------------
# 지원 언어
# --------------------------------------------------

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


# --------------------------------------------------
# 플랫폼 정보
# --------------------------------------------------

PLATFORMS = {
    "baekjoon": {
        "label": "백준",
        "url_template": "https://www.acmicpc.net/problem/{num}",
    },
    "programmers": {
        "label": "프로그래머스",
        "url_template": (
            "https://school.programmers.co.kr/"
            "learn/courses/30/lessons/{num}"
        ),
    },
    "unknown": {
        "label": "미확인 플랫폼",
        "url_template": None,
    },
}


# --------------------------------------------------
# 플랫폼 / 문제 번호 감지
# --------------------------------------------------

def detect_platform_and_number(filepath: str, content: str):
    """
    플랫폼과 문제 번호를 찾아
    (platform, number) 형태로 반환합니다.
    """

    # 1. 코드 안에 프로그래머스 URL이 있는 경우
    match = re.search(
        r"programmers\.co\.kr/learn/courses/30/lessons/(\d+)",
        content,
    )

    if match:
        return "programmers", match.group(1)

    # 2. 코드 안에 백준 URL이 있는 경우
    match = re.search(
        r"acmicpc\.net/problem/(\d+)",
        content,
    )

    if match:
        return "baekjoon", match.group(1)

    # 3. 코드 상단 주석 확인
    header = "\n".join(content.splitlines()[:15])

    match = re.search(
        r"(?:프로그래머스|programmers)\D{0,10}(\d{3,7})",
        header,
        re.IGNORECASE,
    )

    if match:
        return "programmers", match.group(1)

    match = re.search(
        r"(?:백준|BOJ)\D{0,10}(\d{3,7})",
        header,
        re.IGNORECASE,
    )

    if match:
        return "baekjoon", match.group(1)

    # 4. 파일명에서 문제 번호 탐색
    filename = os.path.basename(filepath)
    stem = os.path.splitext(filename)[0]

    if re.fullmatch(r"\d{3,7}", stem):
        return "unknown", stem

    match = re.search(r"(\d{3,7})", stem)

    if match:
        return "unknown", match.group(1)

    # 5. 전체 경로에서도 숫자 탐색
    # 예: 프로그래머스/12909/solution.py
    path_numbers = re.findall(r"(?<!\d)(\d{3,7})(?!\d)", filepath)

    if path_numbers:
        return "unknown", path_numbers[-1]

    return None, None


# --------------------------------------------------
# 문제 제목 가져오기
# --------------------------------------------------

def fetch_problem_title(platform: str, number: str):
    """
    프로그래머스 / 백준 사이트에서 문제 제목을 가져옵니다.
    실패하면 None을 반환합니다.
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(compatible; coding-blog-draft-bot/1.0)"
        )
    }

    try:

        if platform == "baekjoon":

            url = f"https://www.acmicpc.net/problem/{number}"

            response = requests.get(
                url,
                timeout=5,
                headers=headers,
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser",
            )

            title_tag = soup.select_one("#problem_title")

            if title_tag:
                return title_tag.get_text(strip=True)

        elif platform == "programmers":

            url = (
                "https://school.programmers.co.kr/"
                f"learn/courses/30/lessons/{number}"
            )

            response = requests.get(
                url,
                timeout=5,
                headers=headers,
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser",
            )

            if soup.title and soup.title.string:

                raw_title = soup.title.string.strip()

                # 예:
                # 코딩테스트 연습 - 올바른 괄호 | 프로그래머스 스쿨
                match = re.search(
                    r"-\s*(.+?)\s*\|",
                    raw_title,
                )

                if match:
                    return match.group(1).strip()

                return raw_title

    except Exception as error:

        print(
            f"[WARN] {platform} {number} 문제 제목 "
            f"가져오기 실패: {error}"
        )

    return None


# --------------------------------------------------
# OpenAI API 분석
# --------------------------------------------------

def analyze_with_openai(
    platform: str,
    number: str,
    title: str,
    code: str,
):
    """
    실제 풀이 코드를 OpenAI API에 전달하여
    접근 방법 / 시간복잡도 / 회고를 작성합니다.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print(
            "[WARN] OPENAI_API_KEY가 없습니다. "
            "AI 분석을 건너뜁니다."
        )
        return None

    client = OpenAI(api_key=api_key)

    platform_label = PLATFORMS.get(
        platform,
        PLATFORMS["unknown"],
    )["label"]

    prompt = f"""
너는 코딩테스트 풀이를 분석해 개발 블로그 초안을 작성하는 도우미다.

아래 코드는 사용자가 실제로 작성한 풀이 코드다.

코드를 정확하게 읽고,
코드에 실제로 존재하는 로직만 근거로 설명해야 한다.

사용자가 하지 않은 생각이나 시행착오를 만들어내면 안 된다.

예를 들어 코드에 deque가 있다고 해서 무조건 BFS라고 판단하는 식의
단순 패턴 추측을 하지 말고 실제 제어 흐름과 자료구조 사용 목적을 분석한다.

문제 정보

- 플랫폼: {platform_label}
- 문제 번호: {number}
- 문제 제목: {title}

사용자가 작성한 코드:

--- CODE START ---

{code}

--- CODE END ---


다음 세 개의 Markdown 섹션을 반드시 작성한다.


## 접근 방법

실제 코드가 문제를 어떤 방식으로 해결하는지 설명한다.

다음 내용을 자연스러운 블로그 글 형태로 작성한다.

- 핵심 아이디어
- 사용한 알고리즘 또는 자료구조
- 코드가 어떤 순서로 동작하는지

코드에서 확인할 수 없는 사용자의 생각이나 시행착오는
절대로 만들어내지 않는다.


## 시간복잡도

다음 내용을 작성한다.

- 시간복잡도
- 공간복잡도
- 각각 그렇게 판단한 이유

Big-O 표기법을 사용한다.


## 회고

단순히 "좋은 문제였다" 같은 일반적인 내용은 작성하지 않는다.

실제 코드를 기반으로 다음 내용을 분석한다.

- 이 풀이에서 배울 수 있는 점
- 불필요하거나 복잡하게 작성된 부분
- 놓친 예외 케이스
- 논리 오류 가능성
- 더 단순하거나 안전하게 작성할 수 있는 방법

특히 현재 코드가 특정 입력에서 잘못된 결과를 반환할 가능성이 있다면
반드시 구체적인 예시를 들어 설명한다.

단, 정답 코드를 새로 작성하지는 않는다.


작성 규칙

- 한국어로 작성한다.
- 개발자가 직접 정리한 블로그 글처럼 자연스럽게 쓴다.
- 지나치게 장황하게 작성하지 않는다.
- 존댓말을 사용하지 않는다.
- "사용자는"이라는 표현을 사용하지 않는다.
- "AI가 분석한 결과" 같은 표현을 사용하지 않는다.
- 전체 결과를 코드 블록(```)으로 감싸지 않는다.
- 반드시 아래 세 제목만 출력한다.

## 접근 방법
## 시간복잡도
## 회고
"""

    try:

        print(
            f"[AI] {platform_label} {number} "
            f"'{title}' 코드 분석 요청"
        )

        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )

        analysis = response.output_text.strip()

        if not analysis:
            print("[WARN] AI 분석 결과가 비어 있습니다.")
            return None

        print("[AI] 코드 분석 완료")

        return analysis

    except Exception as error:

        print(
            f"[WARN] OpenAI API 분석 실패: {error}"
        )

        return None


# --------------------------------------------------
# AI 호출 실패 시 TODO
# --------------------------------------------------

def build_fallback_analysis():

    return """## 접근 방법

**TODO:** 문제를 어떻게 접근했는지 작성해주세요.

## 시간복잡도

**TODO:** 시간복잡도와 공간복잡도를 작성해주세요.

## 회고

**TODO:** 풀면서 배운 점이나 개선할 부분을 작성해주세요."""


# --------------------------------------------------
# Markdown 생성
# --------------------------------------------------

def build_markdown(
    platform: str,
    number: str,
    title: str,
    language: str,
    code: str,
    source_path: str,
    ai_analysis: str | None,
):
    platform_info = PLATFORMS.get(
        platform,
        PLATFORMS["unknown"],
    )

    platform_label = platform_info["label"]
    url_template = platform_info["url_template"]

    if url_template:
        url = url_template.format(num=number)
    else:
        url = None

    today = (
        datetime.now(timezone.utc)
        .astimezone()
        .strftime("%Y-%m-%d")
    )

    if url:
        link_line = f"- 문제 링크: {url}"
    else:
        link_line = (
            "- 문제 링크: **TODO** "
            "(플랫폼을 자동으로 판별하지 못했습니다.)"
        )

    platform_note = ""

    if platform == "unknown":
        platform_note = (
            "\n> ⚠️ 문제 번호는 찾았지만 플랫폼을 "
            "자동으로 판별하지 못했습니다.\n"
        )

    if not ai_analysis:
        ai_analysis = build_fallback_analysis()

    markdown = (
        f"# [{platform_label} {number}] {title} 풀이\n\n"
        f"{link_line}\n"
        f"- 사용 언어: {language}\n"
        f"- 원본 코드: `{source_path}`\n"
        f"- 생성일: {today}\n"
        f"{platform_note}\n"
        "## 문제 설명\n\n"
        f"> {title}\n"
        ">\n"
        "> 자세한 문제 설명과 제약 조건은 위 문제 링크를 참고한다.\n\n"
        f"{ai_analysis}\n\n"
        "## 코드\n\n"
        f"```{language}\n"
        f"{code}\n"
        "```\n\n"
        "---\n\n"
        "*이 글은 풀이 코드가 push될 때 자동 생성된 초안이다. "
        "게시 전 내용을 한 번 확인한다.*\n"
    )

    return markdown

# --------------------------------------------------
# main
# --------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("사용법: python analyze_solution.py changed_files.txt")
        sys.exit(1)

    changed_files_path = sys.argv[1]

    with open(changed_files_path, encoding="utf-8") as file:
        changed_files = [
            line.strip()
            for line in file
            if line.strip()
        ]

    print(f"[INFO] 변경 파일 {len(changed_files)}개 감지")

    os.makedirs("blog-drafts", exist_ok=True)
    generated = []

    for filepath in changed_files:
        print(f"[CHECK] {filepath}")

        if filepath.startswith("blog-drafts/"):
            print("[SKIP] blog-drafts 파일")
            continue

        if not os.path.exists(filepath):
            print(f"[SKIP] 파일이 존재하지 않음: {filepath}")
            continue

        ext = os.path.splitext(filepath)[1].lower()

        if ext not in EXT_LANG:
            print(f"[SKIP] 지원하지 않는 확장자: {ext}")
            continue

        with open(filepath, encoding="utf-8", errors="ignore") as file:
            content = file.read()

        platform, number = detect_platform_and_number(filepath, content)

        if not number:
            print(f"[SKIP] {filepath}: 문제 번호를 찾을 수 없습니다.")
            continue

        language = EXT_LANG[ext]
        title = fetch_problem_title(platform, number) or f"{number}번 문제"

        print(f"[INFO] 문제 감지: {platform} / {number} / {title}")

        ai_analysis = analyze_with_openai(
            platform,
            number,
            title,
            content,
        )

        markdown = build_markdown(
            platform=platform,
            number=number,
            title=title,
            language=language,
            code=content,
            source_path=filepath,
            ai_analysis=ai_analysis,
        )

        output_path = f"blog-drafts/{platform}-{number}.md"

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(markdown)

        generated.append(output_path)
        print(f"[OK] {output_path} 생성 완료")

    if not generated:
        print("생성된 초안이 없습니다. (이번 push에서 분석 가능한 풀이 파일 없음)")
        return

    print()
    print("===== 생성 완료 =====")

    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
