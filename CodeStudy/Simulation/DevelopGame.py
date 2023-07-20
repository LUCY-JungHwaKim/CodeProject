# # ##### 이게 내가 작성한 코드
n, m = map(int, input().split())

x,y, dloc = map(int, input().split())

map_ary = [list(map(int, input().split())) for _ in range(n)]

print(map_ary)

dx = [-1, 0, 1,0] #북동남서
dy = [0,  1, 0, -1]

back_r = [2, 3, 0, 1] ## 뒤로 가는 방향

## 방문 위치 저장하는 배열
d = [[0]*m for _ in range(n)]
d[x][y] = 1 ## 현재 위치 방문 처리

no_route = 0
go_cnt = 1 # 처음시작이니깐 1


while True:

    dloc -= 1

    if dloc == -1:
        dloc = 3

    curx = x + dx[dloc]
    cury = y + dy[dloc]



    if map_ary[curx][cury] == 0 and d[curx][cury] == 0: ## 가보지 않은 칸이 존재한다면, 육지 칸인 경우
        x,y = curx, cury
        d[x][y] = 1 ## 갔다고 표시 (방문 표시)
        go_cnt += 1
        no_route = 0 ## 네 방향 탐색을 다 했다는ㄴ 것을 표시하기 위한 변수
    else:
        no_route += 1



    if no_route == 4:
        curx = x+ dx[back_r[dloc]]
        cury  = y +dy[back_r[dloc]] ## 뒤 돌기

        if map_ary[curx][cury] == 0: ## 육지인 경우 
            x,y = curx, cury
        else:
            break
        no_route = 0



print(go_cnt)


