from collections import deque

T = int(input())


def findbaechu(ary, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    ary[x][y] = 0  ## 배추 없는 것으로 표시

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    rslt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or ary[nx][ny] == 0 or visited[nx][ny] == True:
                continue
                ## 범위를 벗어나거나, 0이거나 1인데 이미 방문했거나

            if ary[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                rslt += 1
                ary[nx][ny] = 0

    return rslt


for _ in range(T):
    m, n, k = map(int, input().split())  ## 가로 세로
    ary = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        ary[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if ary[i][j] == 1:  ## 1인거 발견하면 가라
                rslt = findbaechu(ary, i, j, visited)
                if rslt > 0:
                    cnt += 1

    print(cnt)