from collections import deque

n = int(input())
bomb_lst = [list(map(str, input())) for _ in range(n)] ## 폭탄 입력
cur_loc = [list(map(str, input())) for _ in range(n)] ## 지뢰찾기 게임에서 누른거 위치 기록용

## 상하 좌우, 대각선 옮기기
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
bombloc = [] ## 폭탄 위치 기록용
for i in range(n):
    for j in range(n):
        if bomb_lst[i][j] == '*':
            bombloc.append((i, j)) ## 추후에 지뢰가 열렸을 때, 모든 지뢰를 표시해야하므로 .. 이를 위한 지뢰위치 기록용

visited = [[False for _ in range(n)] for _ in range(n)]

bombq = deque()
x, y = 0, 0
bombq.append((x, y))
bmbmaps = [['.' for _ in range(n)] for _ in range(n)]
chkbmb = 0 ## 지뢰가 한번이라도 눌러졌는지 체크
## 만약 지뢰를 눌렀다면, 지뢰가 있는 모든 칸에서 지뢰를 보여줘야 함

while bombq:

    nx, ny = bombq.popleft()
    visited[nx][ny] = True
    bmbcnt = 0

    if (bomb_lst[nx][ny] == '*') & (cur_loc[nx][ny] == 'x'):
        ## 현재 열린자리에 폭탄이 있는거라면?
        chkbmb = 1
        bmbmaps[nx][ny] = '*'


    for i in range(len(dx)): ## 8방향 탐색
        cx = nx + dx[i]
        cy = ny + dy[i]


        if cx < 0 or cx >= n or cy < 0 or cy >= n: ## 다음 이동 방향이 범위 넘으면 탐색 금지
            continue

        if (visited[cx][cy] == True) & (bomb_lst[cx][cy] == '*'): ## 만약 범위 탐색 중 이미 갔던곳인데, 폭탄이 있다면
            ## 그냥 폭탄 수 카운트 
            bmbcnt += 1
            continue

        if visited[cx][cy] == False: ## 만약 간곳이 아니라면

            ## 다음 자리에 만약에 폭탄이 있다면?
            if (bomb_lst[cx][cy] == '*'): ## 간곳이 아닌데 폭탄이 있다. 그럼 이때도 폭탄 수 카운트
                bmbcnt += 1
            ## 어쨌든 간곳은 방문 표시해주고, 큐에 넣어줌
            visited[cx][cy] = True
            bombq.append((cx, cy))

    if cur_loc[nx][ny] == 'x':# 열었는데
        if (bomb_lst[nx][ny] == '.'): # 폭탄이 아닌경우에는
            bmbmaps[nx][ny] = bmbcnt # 숫자 삽입

if chkbmb == 1: ## 지뢰가 한번이라도 눌러졌다는 거임
    for i in range(len(bombloc)):
        bx, by = bombloc[i][0], bombloc[i][1]
        bmbmaps[bx][by] = '*'

for i in range(n):
    for j in range(n):
        if j == n - 1:
            print(bmbmaps[i][j])
        else:
            print(bmbmaps[i][j], end='')