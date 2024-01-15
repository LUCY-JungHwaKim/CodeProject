from collections import deque

c, r, h = map(int, input().split())
totalary = []
for _ in range(h):
    ary = []
    for _ in range(r):
        ary.append(list(map(int, input().split())))
    totalary.append(ary)

q = deque()
cnt = 0
for i in range(h):
    for j in range(r):
        for x in range(c):
            if totalary[i][j][x] == 1:  ##토마토가 있을때
                q.append((i, j, x))

            if totalary[i][j][x] != 0:  ## -1이나 1인 ㄱ경우에
                cnt += 1

# print(totalary[1])

dx = [-1, 1, 0, 0, 0, 0]  ##h
dy = [0, 0, -1, 1, 0, 0]  ##r
dz = [0, 0, 0, 0, -1, 1]  ##c

visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(h)]


def bfs(totalary, visited, q):
    while q:
        cx, cy, cz = q.popleft()  ##h,r,c
        visited[cx][cy][cz] = True

        for i in range(len(dx)):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]

            if (0 <= nx < h) and (0 <= ny < r) and (0 <= nz < c) and visited[nx][ny][nz] == False:
                # print(nx,ny,nz)
                # print(totalary[nx][ny][nz])
                if totalary[nx][ny][nz] == 0:  # 안익은 토마토 있을때
                    totalary[nx][ny][nz] = totalary[cx][cy][cz] + 1
                    q.append((nx, ny, nz))
                    visited[nx][ny][nz] = True

    max_rslt = -99999
    for i in range(h):
        for j in range(r):
            for x in range(c):
                if totalary[i][j][x] == 0:  ## 하나라도 안 익어있다면
                    print(-1)
                    return
                max_rslt = max(max_rslt, totalary[i][j][x])

    print(max_rslt - 1)
    return


if cnt == (h * r * c):
    print(0)
else:
    bfs(totalary, visited, q)