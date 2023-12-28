n, m, k = map(int, input().split())
ary = []
sx, sy = n - 1, 0  ## 항상 시작 좌표는 왼쪽 아래 라고 했음

for i in range(n):
    ary.append(list(map(str, input())))

dx = [0, 0, 1, -1]  ## 동, 서, 남, 북
dy = [1, -1, 0, 0]

stk = []
cnt = 0


def dfs(graph, x, y, sol):
    global cnt

    # print(sol)

    if (x == 0 and y == m - 1) and (len(sol) == k):
        cnt += 1
        return

    for i in range(len(dx)):  ## 4방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or ary[nx][ny] == 'T':  ## 자리 넘으면 안함, T면 안감
            continue

        sol.append((nx, ny))
        ary[nx][ny] = 'T'
        dfs(graph, nx, ny, sol)
        px, py = sol.pop()
        ary[px][py] = '.'


stk.append((sx, sy))
ary[sx][sy] = 'T'  ## 초기 시작점 방문 여부도 확인해줘야함
dfs(ary, sx, sy, stk)
print(cnt)