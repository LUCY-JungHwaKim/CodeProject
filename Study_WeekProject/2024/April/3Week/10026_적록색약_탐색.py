from collections import deque


def normalsearch():
    rslt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and ary[nx][ny] == ary[cx][cy]:
                q.append((nx, ny))
                visited[nx][ny] = True
                rslt += 1

    return rslt


if __name__ == "__main__":
    N = int(input())

    ary = []

    for _ in range(N):
        ary.append(list(map(str, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    normlst = []
    q = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                q.append((i, j))
                visited[i][j] = True
                rsltvalue = normalsearch()

                normlst.append(rsltvalue)

    falnorm = []

    for i in range(N):
        for j in range(N):
            if ary[i][j] == 'R':
                ary[i][j] = 'G'
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                q.append((i, j))
                visited[i][j] = True
                rsltvalue = normalsearch()

                falnorm.append(rsltvalue)

    print("{} {}".format(len(normlst), len(falnorm)))