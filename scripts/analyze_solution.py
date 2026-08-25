#!/usr/bin/env python3

"""
Push된 코딩테스트 풀이 코드를 분석하여 블로그 초안을 자동 생성합니다.

생성 예시
원본:
    프로그래머스/8m/4w/12909.py

생성:
    blog-drafts/프로그래머스/8m/4w/12909.md
    blog-drafts/프로그래머스/8m/4w/12909.html

동작 과정
1. push된 파일 목록 확인
2. 문제 플랫폼 / 번호 감지
3. 문제 제목 가져오기
4. OpenAI API로 실제 풀이 코드 분석
5. 구조화된 분석 결과 생성
6. GitHub용 Markdown + 티스토리용 HTML 생성
"""

import html
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from openai import OpenAI


EXT_LANG = {
    ".py": "Python",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".c": "C",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".kt": "Kotlin",
    ".go": "Go",
    ".rs": "Rust",
}

CODE_FENCE_LANG = {
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


def detect_platform_and_number(filepath: str, content: str):
    match = re.search(
        r"programmers\.co\.kr/learn/courses/30/lessons/(\d+)", content
    )
    if match:
        return "programmers", match.group(1)

    match = re.search(r"acmicpc\.net/problem/(\d+)", content)
    if match:
        return "baekjoon", match.group(1)

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

    stem = Path(filepath).stem
    if re.fullmatch(r"\d{3,7}", stem):
        return "unknown", stem

    match = re.search(r"(\d{3,7})", stem)
    if match:
        return "unknown", match.group(1)

    path_numbers = re.findall(r"(?<!\d)(\d{3,7})(?!\d)", filepath)
    if path_numbers:
        return "unknown", path_numbers[-1]

    return None, None


def fetch_problem_title(platform: str, number: str):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; coding-blog-draft-bot/1.0)"}

    try:
        if platform == "baekjoon":
            response = requests.get(
                f"https://www.acmicpc.net/problem/{number}",
                timeout=5,
                headers=headers,
            )
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            title_tag = soup.select_one("#problem_title")
            if title_tag:
                return title_tag.get_text(strip=True)

        elif platform == "programmers":
            response = requests.get(
                f"https://school.programmers.co.kr/learn/courses/30/lessons/{number}",
                timeout=5,
                headers=headers,
            )
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            if soup.title and soup.title.string:
                raw_title = soup.title.string.strip()
                match = re.search(r"-\s*(.+?)\s*\|", raw_title)
                if match:
                    return match.group(1).strip()
                return raw_title

    except Exception as error:
        print(f"[WARN] {platform} {number} 문제 제목 가져오기 실패: {error}")

    return None


def _extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", text)
        if not match:
            raise
        return json.loads(match.group(0))


def analyze_with_openai(platform: str, number: str, title: str, code: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[WARN] OPENAI_API_KEY가 없습니다. AI 분석을 건너뜁니다.")
        return None

    client = OpenAI(api_key=api_key)
    platform_label = PLATFORMS.get(platform, PLATFORMS["unknown"])["label"]

    prompt = f"""
너는 코딩테스트 풀이 코드를 읽고 개발 블로그용 분석 데이터를 만드는 도우미다.
반드시 실제 코드에 근거해서만 분석하고, 사용자가 하지 않은 생각이나 시행착오를 지어내지 마라.
단순히 deque가 있다는 이유로 BFS라고 판단하는 식의 패턴 추측은 금지한다.

문제 정보
- 플랫폼: {platform_label}
- 문제 번호: {number}
- 문제 제목: {title}

코드
--- CODE START ---
{code}
--- CODE END ---

아래 JSON 형식만 출력하라. Markdown 코드펜스는 쓰지 마라.
모든 배열 항목은 짧고 개조식으로 작성한다.

{{
  "types": ["Stack", "문자열"],
  "approach": [
    "핵심 동작 1",
    "핵심 동작 2",
    "핵심 동작 3"
  ],
  "key_idea": "이 풀이의 핵심 아이디어를 1~2문장으로 설명",
  "time_complexity": "O(N)",
  "time_reason": "왜 이 시간복잡도인지 짧게 설명",
  "space_complexity": "O(N)",
  "space_reason": "왜 이 공간복잡도인지 짧게 설명",
  "good_points": [
    "코드에서 잘 적용한 점"
  ],
  "issues": [
    {{
      "title": "문제 또는 주의점 제목",
      "detail": "실제 코드에서 왜 문제가 되는지 설명",
      "example": "구체적인 반례가 있으면 입력 예시, 없으면 빈 문자열"
    }}
  ],
  "improvements": [
    "더 단순하거나 안전하게 구현할 수 있는 방향"
  ],
  "retrospective": [
    "이 코드에서 복습할 핵심 포인트"
  ]
}}

작성 규칙
- 한국어로 작성한다.
- 문장 끝은 '~함', '~가능', '~필요'처럼 개조식 위주로 작성한다.
- types는 실제 사용한 알고리즘/자료구조만 넣는다.
- 코드에 논리 오류나 놓친 예외 케이스가 있으면 issues에 반드시 포함한다.
- 문제가 없다면 issues는 빈 배열로 둔다.
- 반례를 확실히 제시할 수 있을 때만 example을 채운다.
- 정답 코드를 새로 작성하지 않는다.
- 과장된 평가나 감상문은 쓰지 않는다.
"""

    try:
        print(f"[AI] {platform_label} {number} '{title}' 코드 분석 요청")
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )
        result = _extract_json(response.output_text)
        print("[AI] 코드 분석 완료")
        return result

    except Exception as error:
        print(f"[WARN] OpenAI API 분석 실패: {error}")
        return None


def fallback_analysis():
    return {
        "types": ["미분류"],
        "approach": ["TODO: 접근 방법 작성 필요"],
        "key_idea": "TODO: 핵심 아이디어 작성 필요",
        "time_complexity": "TODO",
        "time_reason": "시간복잡도 분석 필요",
        "space_complexity": "TODO",
        "space_reason": "공간복잡도 분석 필요",
        "good_points": [],
        "issues": [],
        "improvements": [],
        "retrospective": ["TODO: 회고 작성 필요"],
    }


def normalize_analysis(data):
    if not isinstance(data, dict):
        return fallback_analysis()

    base = fallback_analysis()
    for key in base:
        if key in data and data[key] is not None:
            base[key] = data[key]

    for key in ["types", "approach", "good_points", "issues", "improvements", "retrospective"]:
        if not isinstance(base[key], list):
            base[key] = []

    return base


def problem_url(platform: str, number: str):
    template = PLATFORMS.get(platform, PLATFORMS["unknown"])["url_template"]
    return template.format(num=number) if template else None


def build_markdown(platform, number, title, language, fence_language, code, source_path, analysis):
    platform_label = PLATFORMS.get(platform, PLATFORMS["unknown"])["label"]
    url = problem_url(platform, number)
    types = " / ".join(analysis["types"]) if analysis["types"] else "미분류"

    lines = [
        f"# [{platform_label} {number}] {title}",
        "",
        f"- 문제 링크: {url or 'TODO'}",
        f"- 사용 언어: {language}",
        f"- 문제 유형: {types}",
        f"- 원본 코드: `{source_path}`",
        "",
        "## 💡 접근 방법",
        "",
    ]

    for item in analysis["approach"]:
        lines.append(f"- {item}")

    lines += [
        "",
        "### 📌 핵심 아이디어",
        "",
        analysis["key_idea"],
        "",
        "## 💻 코드",
        "",
        f"```{fence_language}",
        code.rstrip(),
        "```",
        "",
        "## ⏱️ 시간 · 공간 복잡도",
        "",
        f"- **시간복잡도: `{analysis['time_complexity']}`**",
        f"  - {analysis['time_reason']}",
        f"- **공간복잡도: `{analysis['space_complexity']}`**",
        f"  - {analysis['space_reason']}",
        "",
        "## 🔎 코드 리뷰",
        "",
    ]

    if analysis["good_points"]:
        lines += ["### 잘 적용한 부분", ""]
        lines.extend(f"- {item}" for item in analysis["good_points"])
        lines.append("")

    if analysis["issues"]:
        lines += ["### ⚠️ 확인이 필요한 부분", ""]
        for issue in analysis["issues"]:
            if not isinstance(issue, dict):
                continue
            title_text = issue.get("title", "확인 필요")
            detail = issue.get("detail", "")
            example = issue.get("example", "")
            lines.append(f"- **{title_text}**")
            if detail:
                lines.append(f"  - {detail}")
            if example:
                lines.append(f"  - 예: `{example}`")
        lines.append("")

    if analysis["improvements"]:
        lines += ["### 🔧 개선 방향", ""]
        lines.extend(f"- {item}" for item in analysis["improvements"])
        lines.append("")

    lines += ["## 📝 회고", ""]
    lines.extend(f"- {item}" for item in analysis["retrospective"])
    lines += ["", "---", "", "*풀이 코드를 기반으로 자동 생성한 초안입니다.*", ""]

    return "\n".join(lines)


def html_list(items):
    if not items:
        return ""
    return '<ul style="line-height: 1.9;">' + "".join(
        f"<li>{html.escape(str(item))}</li>" for item in items
    ) + "</ul>"


def build_html(platform, number, title, language, code, analysis):
    platform_label = PLATFORMS.get(platform, PLATFORMS["unknown"])["label"]
    url = problem_url(platform, number)
    types = " / ".join(analysis["types"]) if analysis["types"] else "미분류"

    if url:
        problem_line = (
            f'<a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">'
            f'{html.escape(platform_label)} - {html.escape(title)}</a>'
        )
    else:
        problem_line = f"{html.escape(platform_label)} - {html.escape(title)}"

    parts = [
        '<div style="padding: 16px 20px; margin: 20px 0; background: #f7f7f8; border-radius: 10px; line-height: 1.8;">',
        f"<b>🔗 문제</b> : {problem_line}<br>",
        f"<b>💻 언어</b> : {html.escape(language)}<br>",
        f"<b>🏷️ 유형</b> : {html.escape(types)}",
        "</div>",
        "",
        "<h2>💡 접근 방법</h2>",
        html_list(analysis["approach"]),
        "",
        "<h3>📌 핵심 아이디어</h3>",
        '<div style="padding: 16px 20px; margin: 16px 0; border-left: 4px solid #555; background: #f8f8f8; line-height: 1.8;">',
        html.escape(str(analysis["key_idea"])),
        "</div>",
        "",
        "<h2>💻 코드</h2>",
        '<pre style="padding: 20px; overflow-x: auto; border-radius: 10px; background: #272822; color: #f8f8f2; line-height: 1.6;"><code>',
        html.escape(code.rstrip()),
        "</code></pre>",
        "",
        "<h2>⏱️ 시간 · 공간 복잡도</h2>",
        '<div style="padding: 16px 20px; margin: 16px 0; background: #f7f7f8; border-radius: 10px; line-height: 1.8;">',
        f"<p><b>시간복잡도 : {html.escape(str(analysis['time_complexity']))}</b></p>",
        f"<ul><li>{html.escape(str(analysis['time_reason']))}</li></ul>",
        f"<p><b>공간복잡도 : {html.escape(str(analysis['space_complexity']))}</b></p>",
        f"<ul><li>{html.escape(str(analysis['space_reason']))}</li></ul>",
        "</div>",
        "",
        "<h2>🔎 코드 리뷰</h2>",
    ]

    if analysis["good_points"]:
        parts += ["<h3>잘 적용한 부분</h3>", html_list(analysis["good_points"]), ""]

    if analysis["issues"]:
        parts += ["<h3>⚠️ 확인이 필요한 부분</h3>"]
        for issue in analysis["issues"]:
            if not isinstance(issue, dict):
                continue
            issue_title = html.escape(str(issue.get("title", "확인 필요")))
            detail = html.escape(str(issue.get("detail", "")))
            example = str(issue.get("example", "") or "")

            issue_html = [
                '<div style="padding: 16px 20px; margin: 16px 0; background: #fff8e6; border-left: 4px solid #e5a100; border-radius: 4px; line-height: 1.8;">',
                f"<b>{issue_title}</b>",
            ]
            if detail:
                issue_html += ["<br><br>", detail]
            if example:
                issue_html += [
                    "<br><br>",
                    '<b>반례 예시</b>',
                    f'<pre style="padding: 12px; background: #ffffff; border-radius: 6px; overflow-x: auto;"><code>{html.escape(example)}</code></pre>',
                ]
            issue_html.append("</div>")
            parts.extend(issue_html)

    if analysis["improvements"]:
        parts += ["<h3>🔧 개선 방향</h3>", html_list(analysis["improvements"]), ""]

    parts += [
        "<h2>📝 회고</h2>",
        html_list(analysis["retrospective"]),
        "",
        '<hr style="margin: 40px 0;">',
        '<p style="font-size: 13px; color: #888;">풀이 코드를 기반으로 자동 생성한 초안입니다.</p>',
        "",
    ]

    return "\n".join(parts)


def output_paths(source_path: str):
    source = Path(source_path)
    relative_no_suffix = source.with_suffix("")
    base = Path("blog-drafts") / relative_no_suffix
    return base.with_suffix(".md"), base.with_suffix(".html")


def main():
    if len(sys.argv) < 2:
        print("사용법: python analyze_solution.py changed_files.txt")
        sys.exit(1)

    changed_files_path = sys.argv[1]
    with open(changed_files_path, encoding="utf-8") as file:
        changed_files = [line.strip() for line in file if line.strip()]

    print(f"[INFO] 변경 파일 {len(changed_files)}개 감지")
    generated = []

    for filepath in changed_files:
        print(f"[CHECK] {filepath}")

        if filepath.startswith("blog-drafts/"):
            print("[SKIP] blog-drafts 파일")
            continue

        if not os.path.exists(filepath):
            print(f"[SKIP] 파일이 존재하지 않음: {filepath}")
            continue

        ext = Path(filepath).suffix.lower()
        if ext not in EXT_LANG:
            print(f"[SKIP] 지원하지 않는 확장자: {ext}")
            continue

        with open(filepath, encoding="utf-8", errors="ignore") as file:
            content = file.read()

        platform, number = detect_platform_and_number(filepath, content)
        if not number:
            print(f"[SKIP] {filepath}: 문제 번호를 찾을 수 없습니다.")
            continue

        title = fetch_problem_title(platform, number) or f"{number}번 문제"
        language = EXT_LANG[ext]
        fence_language = CODE_FENCE_LANG[ext]

        print(f"[INFO] 문제 감지: {platform} / {number} / {title}")

        analysis = normalize_analysis(
            analyze_with_openai(platform, number, title, content)
        )

        markdown = build_markdown(
            platform,
            number,
            title,
            language,
            fence_language,
            content,
            filepath,
            analysis,
        )
        tistory_html = build_html(
            platform,
            number,
            title,
            language,
            content,
            analysis,
        )

        md_path, html_path = output_paths(filepath)
        md_path.parent.mkdir(parents=True, exist_ok=True)

        md_path.write_text(markdown, encoding="utf-8")
        html_path.write_text(tistory_html, encoding="utf-8")

        generated.extend([str(md_path), str(html_path)])
        print(f"[OK] {md_path} 생성 완료")
        print(f"[OK] {html_path} 생성 완료")

    if not generated:
        print("생성된 초안이 없습니다. (이번 push에서 분석 가능한 풀이 파일 없음)")
        return

    print("\n===== 생성 완료 =====")
    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
