from collections import deque
from itertools import combinations

n,m = map(int, input().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virusary = []





for i in range(n):
    for j in range(n):
        if ary[i][j] == 2 : ## 바이러스 놓을 수 있는 칸
            virusary.append((i,j))
rslt = float("inf") # 최소값 찾아야하니깐


def bfs(x): ## 조합별로 찾기
    q = deque(x) ## 한번에 넣기
    #mapary = ary.copy()
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    for a, b in q: ## 방문표시
        visited[a][b] = 0 ## 바이러스 표시
    #rslt = 0

    while q:
        cx, cy = q.popleft()

        for m in range(len(dx)):
            nx = cx + dx[m]
            ny = cy + dy[m]

            if 0 <= nx < n  and 0 <= ny < n:
                if visited[nx][ny] == -1 and ary[nx][ny] != 1:
                    ## 바이러스가 갈수 있꼬, 아직 방문하지 않았다면?
                    q.append([nx, ny])
                    visited[nx][ny] = visited[cx][cy] + 1
                    #print(rslt, visited[cx][cy] + 1)
                    #rslt =  max(rslt,visited[cx][cy] + 1 )



    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and ary[i][j] != 1:
                ## 감염되지 앟은 빈칸이 있다
                return float("inf")


    maxvalue = max(max(a) for a in visited)
    #print(rslt, maxvalue)

    #print("---")
    return maxvalue


for x in combinations(virusary, m):
    rslt = min(rslt, bfs(x))

if rslt == float("inf"):
    print(-1)
else:
    print(rslt)
