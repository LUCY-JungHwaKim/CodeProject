# [프로그래머스 87946] 피로도

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
- 사용 언어: Python
- 문제 유형: 백트래킹 / 재귀 / 리스트
- 원본 코드: `프로그래머스/9m:2w/tired_score.py`

## 💡 접근 방법

- visited 배열로 방문한 던전 표시 후 재귀로 모든 방문 순서 탐색함
- 현재 피로도 k가 던전 최소 필요 피로도 이상이면 진입하여 피로도 감소시키고 방문 카운트 증가시킴
- 재귀 반환 시 visited 플래그를 되돌려 백트래킹으로 다른 순서도 시도함

### 📌 핵심 아이디어

재귀적 백트래킹으로 가능한 모든 던전 방문 순서를 시도하고 방문 개수의 최댓값을 구함

## 💻 코드

```python
## https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    # nonlocal answer
    answer = -1
    curtired = k
    curdun = []
    visited = [False for _ in range(len(dungeons))]

    # curdun.append(dungeons[i])
    visitCnt = 0

    def dfs(k, visitCnt):
        nonlocal answer

        answer = max(answer, visitCnt)

        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and visited[i] == False:
                visited[i] = True
                dfs(k - dungeons[i][1], visitCnt + 1)
                visited[i] = False
            # print(i)

    dfs(k, 0)

    return answer
```

## ⏱️ 시간 · 공간 복잡도

- **시간복잡도: `O(n!)`**
  - 최대 n개의 던전 순열을 모두 탐색하므로 첫 선택 n, 두번째 n-1 ...로 경우의 수가 n!에 비례함
- **공간복잡도: `O(n)`**
  - 재귀 깊이와 visited 배열로 O(n) 보조 공간 사용함

## 🔎 코드 리뷰

### 잘 적용한 부분

- 문제 요구대로 모든 방문 순서를 완전 탐색하여 정답을 보장함
- visited 플래그를 적절히 되돌려 백트래킹을 정확히 구현함
- 현재 방문 수로 즉시 answer를 갱신해 별도 종료 조건 없이 최대값 유지함

### 🔧 개선 방향

- 사용하지 않는 변수(curtired, curdun, 주석된 코드)를 제거해 가독성 향상 필요
- 초기 answer를 0으로 설정해 음수 값 사용 불필요하게 만들기 가능
- itertools.permutations를 사용해 코드가 더 간결해짐(재귀 대신 순열 검사 방식)
- 함수 내부 변수명과 인자명이 같아 가독성이 떨어짐으로 더 명확한 변수명 권장

## 📝 회고

- 백트래킹 패턴: 방문 표시 -> 재귀 호출 -> 방문 취소 순서로 상태 복원 중요함
- 가지치기 조건(k >= 필요 피로도)을 통해 불필요한 경로를 즉시 배제하는 방법 확인함
- 재귀 깊이와 방문 배열의 크기가 동일하므로 공간 복잡도 분석 간단함

---

*풀이 코드를 기반으로 자동 생성한 초안입니다.*
