# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
from collections import deque

n = int(input())

ary = []
for i in range(n):
    ary.append(list(map(int, input())))

dx = [0, 0, 1, -1]  ## 동, 서, 남, 북
dy = [1, -1, 0, 0]


# visited = [[False] * n for _ in range(n)]
## 여기서 주의해야 할 점
## visited = [[False]* n]*n 이라고 하면 안됨
# 왜? --> 리스트를 만들고 그 리스트를 n번 복제하는 방법이기 때문에
## 내부 리스트들이 동일한 객체를 참조하게 됨
## 따라서 하나의 내부 리스트를 수정하면 모든복제된 리스트가 영향을 받게됨 @@ 

## 어디에서 출발할지 모르니깐 만나는 칸은 0으로 바꿔서 두번이상 방문 못하게 하기

def bfs(graph, x, y, n):
    q = deque()
    q.append((x, y))  ## 초기값 초기화
    rslcnt = 1
    ary[x][y] = 0
    # visited[0][0] = True
    # calcnt = 1

    while q:

        nx, ny = q.popleft()

        for i in range(len(dx)):  ## 동서남북탐색
            cx = nx + dx[i]  ## 다음 좌표 지정
            cy = ny + dy[i]

            if cx < 0 or cx >= n or cy < 0 or cy >= n:  ## 정해진 테이블의 크기를 벗어났을 경우 진행안함
                continue  ## 다음꺼 안함

            if ary[cx][cy] == 1:  ## 1인 경우에 0으로 표시하고 (방문했다는 뜻, 이젠 앞으로 방문 안할거야), 큐에 집어넣기
                ary[cx][cy] = 0
                q.append((cx, cy))
                rslcnt += 1

    return rslcnt


cnt = []
for i in range(n):
    for j in range(n):
        if ary[i][j] == 1:  ## 1일 때만 가기
            cnt.append(bfs(ary, i, j, n))  ## 이 안에서 1을 만나면 0으로 다 바꿔버림

print(len(cnt))
cnt.sort()
# print(cnt.sort())
for i in range(len(cnt)):
    print(cnt[i])
