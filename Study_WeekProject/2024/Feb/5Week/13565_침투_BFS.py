from collections import deque
M,N = map(int, input().split())


ary = []

for _ in range(M):
    ary.append(list(map(int, input())))

q = deque()

for i in range(N):
    if ary[0][i] == 0:
        q.append((0,i)) ## 바깥쪽에서 침투 가능한 섬유 위치 삽입

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:

    cx, cy = q.popleft()
    ary[cx][cy] = 2 ## 침투했다는 의미

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0<= nx < M and 0<=ny<N and ary[nx][ny] == 0: ## 침투 가능한 영역
            ary[nx][ny] = 2
            q.append((nx, ny))


cnt = 0
for i in range(N):
    if ary[M-1][i] == 2:
        cnt += 1
        break

if cnt > 0:
    print("YES")
else:
    print("NO")
