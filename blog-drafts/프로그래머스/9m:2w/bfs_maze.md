# [프로그래머스 1844] 게임 맵 최단거리

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
- 사용 언어: Python
- 문제 유형: BFS / Deque / 2D 배열
- 원본 코드: `프로그래머스/9m:2w/bfs_maze.py`

## 💡 접근 방법

- 시작점 (0,0)을 큐에 넣고 BFS 순회함
- 네 방향을 검사하며 방문하지 않은 통로(1)를 큐에 추가하고 방문 표시함
- 방문할 때 원본 maps에 이전 칸 값 더하기로 최단 거리 누적하고 도착점 값 반환함

### 📌 핵심 아이디어

BFS로 각 칸에 도달했을 때의 거리를 원본 maps에 누적해 최단 거리를 계산함

## 💻 코드

```python
## https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))
    n = len(maps)
    m = len(maps[0])

    # print(n,m)

    visited = [[False for _ in range(m)] for _ in range(n)]

    route_cnt = 0

    # for i in range(n):
    #     for j in range(m):
    #         if maps[i][j] == 1:
    #             q.append((i,j)) ## 1,1이 시작

    while q:
        cx, cy = q.popleft()
        visited[cx][cy] = True

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue

            if (maps[nx][ny] == 0):
                continue

            if (maps[nx][ny] != 0 and visited[nx][ny] == False):
                q.append((nx, ny))
                visited[nx][ny] = True
                maps[nx][ny] += maps[cx][cy]
                # print(nx,ny, maps[nx][ny])

    # print(maps[n-1][m-1])
    if maps[n - 1][m - 1] != 1 and visited[n - 1][m - 1] == True:
        return maps[n - 1][m - 1]
    else:
        return -1
    # return answer
```

## ⏱️ 시간 · 공간 복잡도

- **시간복잡도: `O(n*m)`**
  - 각 칸은 최대 한 번 큐에 들어가고 네 방향 확인은 상수 작업이므로 전체 셀 수에 비례함
- **공간복잡도: `O(n*m)`**
  - visited 2D 배열과 최악의 경우 큐에 들어갈 수 있는 모든 셀을 고려하면 공간이 셀 수에 비례함

## 🔎 코드 리뷰

### 잘 적용한 부분

- 방문 시점에 maps에 거리 누적으로 별도 거리 배열 불필요함
- 큐(Deque)로 FIFO 처리하여 최단거리 탐색 구조를 명확히 구현함
- 경계와 벽(0) 체크로 유효한 이동만 처리함
- 방문 표시로 동일 칸 중복 삽입 방지함

### ⚠️ 확인이 필요한 부분

- **출발 칸이 막혀있을 때(start == 0) 처리 누락**
  - 코드는 항상 (0,0)을 큐에 넣고 탐색을 시작하므로 출발 칸이 0(벽)인 입력에서 잘못된 결과(예: 0)를 반환할 가능성이 있음; 출발 칸이 통과불가인지를 사전 검사하지 않음
  - 예: `[[0]]`
- **도착 칸이 초기값(1)인 경우(예: 1x1 맵) 잘못된 반환 조건**
  - 최종 반환 조건에서 maps[n-1][m-1] != 1 을 요구하므로 출발==도착인 1x1 맵 같은 경우 정상적 최단거리 1을 -1로 잘못 반환함
  - 예: `[[1]]`
- **입력 maps를 직접 수정하는 부작용**
  - 거리 누적을 위해 원본 maps 값을 변경하므로 호출자가 원본 맵을 재사용해야 할 경우 문제가 될 수 있음; 입력 불변성을 기대하는 환경에서 부작용 발생 가능

### 🔧 개선 방향

- 시작 칸이 1인지 먼저 검사해 벽이면 즉시 -1 반환하도록 처리함
- 도착이 시작과 같은 경우(1x1) 별도 처리해 1 반환하도록 조건 단순화함
- 원본 maps를 복사하거나 별도 거리 배열을 사용해 입력 변경 부작용 제거함
- 최초 큐 삽입 시점에 visited를 표시하고, 팝 시 다시 표시하는 중복을 제거해 코드 단순화함
- 최종 판정은 visited[n-1][m-1]만 검사하고 방문되었다면 maps 값 반환하도록 변경함

## 📝 회고

- BFS에서 큐에 넣는 시점에 방문 표시하면 중복 삽입 방지 가능함
- 거리 누적을 원본에 할지 별도 배열에 할지 결정해 입력 부작용 고려할 필요 있음
- 엣지 케이스(출발이 막혔거나 시작==도착)는 사전 검사로 깔끔히 처리 가능함
- 최종 반환 조건은 간단명료하게 방문 여부로 판단하는 것이 안전함

---

*풀이 코드를 기반으로 자동 생성한 초안입니다.*
