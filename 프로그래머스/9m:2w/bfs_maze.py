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