from collections import deque


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] == 0:
                ary[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    return cnt


if __name__ == "__main__":
    m, n, k = map(int, input().split())

    ary = [[0 for _ in range(m)] for _ in range(n)]
    locary = []
    rslt = []

    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        locary.append((x1, y1, x2, y2))

    for i in range(len(locary)):
        height = abs(locary[i][0] - locary[i][2])
        width = abs(locary[i][1] - locary[i][3])
        minx, miny = min(locary[i][0], locary[i][2]), min(locary[i][1], locary[i][3])

        for x in range(height):
            for y in range(width):
                ary[minx + x][miny + y] = 1

    q = deque()

    for i in range(n):
        for j in range(m):
            if ary[i][j] == 0:
                q.append((i, j))
                ary[i][j] = 1
                rsltcnt = bfs()
                rslt.append(rsltcnt)

    rslt.sort(key=lambda x: x)
    rslt = list(map(str, rslt))
    print(len(rslt))

    print(' '.join(rslt))

