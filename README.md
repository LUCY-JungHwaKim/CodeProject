# BOJ Blog Draft Generator

백준(BOJ) 풀이 코드를 git push하면, GitHub Actions가 자동으로 코드를 분석해서
**티스토리에 올릴 블로그 글 초안(.md)**을 `blog-drafts/` 폴더에 생성해주는 도구입니다.

> ⚠️ 참고: 티스토리 Open API는 2024년 2월에 완전히 종료되어, 코드를 통한 **완전 자동 발행**은
> 지원하지 않습니다 (공지: https://notice.tistory.com/2664). 대신 이 도구는 초안까지 자동으로
> 만들어주고, 마지막에 사람이 내용을 다듬어 티스토리 에디터에 붙여넣는 방식입니다.

## 동작 방식

1. `main` 브랜치에 풀이 코드를 push합니다.
2. GitHub Actions가 이번 push로 바뀐 파일들을 감지합니다.
3. 파일명 또는 코드 상단 주석에서 **백준 문제 번호**를 찾습니다.
4. acmicpc.net에서 문제 제목을 가져오고, 코드 안의 패턴(BFS/DFS/DP/정렬/이분탐색 등)을
   정규식으로 훑어 "예상 유형"을 추정합니다.
5. `blog-drafts/{문제번호}.md` 파일을 만들어 저장소에 자동 커밋합니다.
6. 여러분은 그 파일을 열어서 `TODO`로 표시된 부분(접근 방법, 시간복잡도, 회고)만
   직접 채운 뒤, 내용을 복사해서 티스토리 글쓰기 화면에 붙여넣으면 됩니다.

## 문제 번호를 인식시키는 방법 (둘 중 하나)

**방법 1. 파일명을 문제 번호로 짓기**

```
sample-solutions/1926.py
sample-solutions/boj_1926.py     (숫자만 포함되어 있어도 인식됨)
```

**방법 2. 코드 상단 주석에 적기** (파일명이 자유로운 경우)

```python
# 백준 1926번 - 그림
...
```

```cpp
// BOJ 1926
...
```

## 지원 언어

`.py .cpp .cc .cxx .c .java .js .ts .kt .go .rs`
(scripts/analyze_solution.py 안의 `EXT_LANG` 딕셔너리에 추가하면 더 늘릴 수 있습니다)

## 로컬에서 미리 테스트해보기

```bash
pip install requests beautifulsoup4
echo "sample-solutions/1926.py" > changed_files.txt
python scripts/analyze_solution.py changed_files.txt
cat blog-drafts/1926.md
```

## 한계 및 향후 개선 방향

- **템플릿/정규식 기반**이라 "어떤 알고리즘을 썼는지"는 추정일 뿐이고, 실제 풀이 논리
  (왜 이렇게 접근했는지, 시행착오, 회고)는 사람이 직접 채워야 합니다.
- 이 부분까지 자동으로 자연스럽게 채우고 싶다면, `scripts/analyze_solution.py`에
  Claude API(또는 다른 LLM API) 호출을 추가해서 코드 설명을 생성하도록 확장할 수 있습니다.
  나중에 필요하시면 이 부분만 이어서 만들어드릴 수 있어요.
- acmicpc.net이 일시적으로 크롤링을 막거나 응답이 없으면 제목은 `"{번호}번 문제"`로
  대체되니, 그 경우 직접 제목을 채워주시면 됩니다.
