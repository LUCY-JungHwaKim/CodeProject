from collections import deque


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[x][y] = 1
    max_dist = 0

    while q:
        cx, cy, dist = q.popleft()
        # print(cx, cy, dis)

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and ary[nx][ny] == 'L':
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = 1
                max_dist = max(max_dist, dist + 1)

    # for i in range(N):
    #     print(*visited[i])
    return max_dist


if __name__ == "__main__":
    N, M = map(int, input().split())

    ary = []

    for _ in range(N):
        ary.append(list(map(str, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    rslt = 0

    for i in range(N):
        for j in range(M):
            if ary[i][j] == 'L':
                rslt = max(rslt, bfs(i, j))

    print(rslt)