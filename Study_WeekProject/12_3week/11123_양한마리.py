from collections import deque
## 단지 번호 붙이기 문제랑 유사

n = int(input())
ary = []
mkary = []

for i in range(n):
    m,k = map(int, input().split())
    mkary.append((m,k))
    tmpary = []
    for j in range(m):
        tmpary.append(list(map(str, input())))
    ary.append(tmpary)

dx = [0, 0, 1, -1] ## 동, 서, 남, 북
dy = [1, -1, 0, 0]

def bfs(graph, x, y, xlen, ylen):
    q = deque()
    q.append((x,y))
    rslt = 1
    graph[x][y] = '.'

    while q:
        cx, cy = q.popleft()

        for m in range(len(dx)):
            nx = cx + dx[m]
            ny = cy + dy[m]

            if nx < 0 or nx >= xlen or ny < 0 or ny >= ylen:
                continue

            if ary[i][nx][ny] == '#':
                q.append((nx, ny))
                ary[i][nx][ny] = '.'
                rslt += 1 ## 연결된 # 개수 카운팅

    return rslt

totalcnt = []
for i in range(n): ## n개 만큼의 양 그리드 확인
    # 양 한마리라도 있으면 하나의 개체로 봄
    
    cnt = []
    for j in range(mkary[i][0]):
        for x in range(mkary[i][1]):
            if ary[i][j][x] == '#': ## #을 만나면 근처 #개수 세아리고, .으로 바꿔주기
                cnt.append(bfs(ary[i], j, x, mkary[i][0], mkary[i][1]))
    totalcnt.append(cnt)

for i in range(len(totalcnt)):
    print(len(totalcnt[i]))
