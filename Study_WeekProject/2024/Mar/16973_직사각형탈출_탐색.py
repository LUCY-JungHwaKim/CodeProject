import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, sys.stdin.readline().split())))

h,w,sx,sy,fx,fy = map(int, sys.stdin.readline().split())
## sx,sy ==> fx,fy로 가야함
visited = [[False for _ in range(m)] for _ in range(n)]
walls = []
for i in range(n):
    for j in range(m):
        if ary[i][j] == 1:
            walls.append((i,j))

dx = [-1, 1, 0, 0] ## 서, 동, 북, 남
dy = [0, 0, -1, 1]
def check(x,y):
    for walx, waly in walls:
        if x<= walx < x + h and y <= waly < y+w:
            return False ## 벽이 있따
    return True ## 벽이 없다

def findroute(cx, cy, cnt): ## 현재 좌표들
    q = deque()
    q.append((cx,cy, cnt))
    visited[cx][cy] = True

    while q:
        curx, cury, cnt = q.popleft()
        #print(curx, cury, cnt)

        if curx == fx -1 and cury == fy-1:
            print(cnt)
            return


        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0<=nx<n and 0<=ny<m and 0<=nx + h -1<n and 0<=ny+w-1<m and visited[nx][ny] == False:
                if check(nx,ny): ## 벽이 있는지 확인해야함
                    q.append((nx,ny, cnt+1))
                    visited[nx][ny] = True

    print(-1)
    return

findroute(sx-1, sy-1, 0)