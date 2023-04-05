n = int(input())


arr = [list(map(int, input())) for _ in range(n)]
visited = [list(map(int, input())) for _ in range(n)]

dx = [0,0, 1, -1] ## 동서 남북
dy = [1,-1,0, 0]

## bFS?



q = []
q.append((0,0))

visited[0][0] = True
cnt = 1

def dfs(r,c):
   r,c = q.pop()

    for i in range=(4):
        nx,ny = r + dx[i], c + dy[i]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            arr[nx][ny] = cnt
            q.append((nx,ny))
            dfs(nx,ny)
        else:
            visited[nx][ny] = True
            q.append((nx,ny))


dfs(0,0)