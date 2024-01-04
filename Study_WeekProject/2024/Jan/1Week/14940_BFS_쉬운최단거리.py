from collections import deque

n, m = map(int, input().split())

ary = []
visited = [[0 for _ in range(m)] for _ in range(n)]
## 여기 사이즈 조절 잘 해줘야함!
## 이것때문에 계속런타임에러 발생하 뮤ㅠㅠ

for i in range(n):
    ary.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if ary[i][j] == 2:
            q.append((i, j))
            visited[i][j] = 1  ## 방문 표시
            ary[i][j] = 0  ## 출발하는 곳이니깐 0으로 초기화

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    cx, cy = q.popleft()

    for i in range(len(dx)):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
            ## 범위를 벗어나거나, 이미 방문된 곳
            continue

        ## 위의 조건에 모두 해당 되지 않으면
        if ary[nx][ny] == 1:  ## 진입 가능한 곳
            ary[nx][ny] = ary[cx][cy] + 1
            q.append((nx, ny))
            visited[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if ary[i][j] != 0 and visited[i][j] == 0:  ## 값 변경이 안된곳 = 진입불가
            ary[i][j] = -1
        print(ary[i][j], end=" ")
    print('')