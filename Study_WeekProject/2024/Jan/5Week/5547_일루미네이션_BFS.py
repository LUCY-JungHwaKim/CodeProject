from collections import deque

m,n = map(int, input().split()) ## 열, 행

ary = [[0] * (m + 2) for _ in range(n+2)] ## 그 주위를 0으로 다 채워주기

for i in range(1, n+1):
    ary[i][1:m+1] = map(int, input().split())

visited = [[False for _ in range(m+2)] for _ in range(n+2)]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    cnt = 0

    dx = [-1, -1, 0, 0, 1, 1]
    dy = [[0, 1, -1, 1, 0, 1], [-1, 0, -1, 1, -1, 0]] ## 홀 짝
    ## 여섯방향은 생각했는데, 홀짝은 생각 못했음
    ## 그리고, 나머지를 0으로 다채워서 1을 만나면 카운트 세는걸 생각해내기가 어려웠음

    while q:
        cx, cy = q.popleft()

        for i in range(len(dx)):
            nx = cx + dx[i]
            if cx % 2 == 1: ## 홀수
                ny = cy + dy[0][i]
            else: #짝수
                ny = cy + dy[1][i]

            if 0<=nx<n+2 and 0<=ny<m+2 : # 주어진 범위에 있을 때,
                ## 0일때, 방문처리랑 좌표 이동해주고 1이면은 전체수 카운트 하면 됨
                if ary[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if ary[nx][ny] == 1:
                    cnt += 1


    print(cnt)

bfs()