from collections import deque

def findB(x,y, strflag):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<M and 0<=ny<N and ary[nx][ny] == strflag and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt



if __name__ == "__main__":

    N,M = map(int, input().split())

    ary = []

    for _ in range(M):
        ary.append(list(map(str, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0 for _ in range(N)] for _ in range(M)]
    Blst = 0
    Wlst = 0
    for i in range(M):
        for j in range(N):
            if ary[i][j] == 'B' and visited[i][j] == 0:
                frsltcnt = findB(i,j,'B')
                Blst += (frsltcnt*frsltcnt)
            if ary[i][j] == 'W' and visited[i][j] == 0:
                Wcnt = findB(i,j,'W')
                Wlst += (Wcnt*Wcnt)

    print("{} {}".format(Wlst, Blst))