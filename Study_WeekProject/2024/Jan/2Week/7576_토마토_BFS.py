from collections import deque

n, m = map(int, input().split())

ary = []

for i in range(m):
    ary.append(list(map(int, input().split())))

tomary = deque()

for i in range(m):
    for j in range(n):
        if ary[i][j] == 1:
            tomary.append((i, j))  ## 토마토 위치 삽입,  얘네를 큐에 삽입


def bfs(ary, tomary):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while tomary:
        cx, cy = tomary.popleft()

        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if ary[nx][ny] == 0:  ## 아직 안익은 토마토가 있따면?
                ary[nx][ny] = ary[cx][cy] + 1
                tomary.append((nx, ny))

    for i in range(m):
        for j in range(n):
            if ary[i][j] == 0:
                return -1

    return ary


rsltary = bfs(ary, tomary)

if rsltary == -1:
    print(-1)
else:
    tmp = []
    for i in range(m):
        tmp.append(max(rsltary[i]))

    print(max(tmp) - 1)