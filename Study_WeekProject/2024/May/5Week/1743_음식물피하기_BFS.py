from collections import deque

def bfs(stx, sty):

    q = deque()

    q.append((stx, sty))
    cnt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<n and 0<=ny<m and ary[nx][ny] == '#':
                ## 범위 내에 있고 음식물 있다면
                ary[nx][ny] = '.'
                q.append((nx, ny))
                cnt += 1

    return cnt

if __name__ == "__main__":
    n,m,k = map(int, input().split())

    ary = [['.' for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0,0]
    dy = [0, 0, -1, 1]
    fincnt = []

    for _ in range(k):
        x,y = map(int, input().split())
        ary[x-1][y-1] = '#'



    for i in range(n):
        for j in range(m):
            if ary[i][j] == '#':
                ary[i][j] = '.' ## 이게 방문 표시임
                cntnum = bfs(i,j)
                fincnt.append(cntnum)

    print(max(fincnt))