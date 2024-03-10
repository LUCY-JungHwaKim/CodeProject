n,m = map(int, input().split())

ary = [[0 for _ in range(m+1)] for _ in range(n+1)]
cnt = 0
def dfs(x,y):
    global cnt
    if (x,y) == (n+1, 1): ## 끝까지 왔다가 다음행으로 내려간것이기 떄문에
        ## 위치가 없는 곳임 그래서 카운팅 하면 됨
        cnt += 1
        return

    if y == m: ## 다음행으로 내려주기
        nx = x+1
        ny = 1
    else:
        nx = x
        ny = y+1

    dfs(nx, ny) ## 현재 위치가 0이고, 다음 위치 보는거

    if ary[x][y-1] == 0 or ary[x-1][y-1] == 0 or ary[x-1][y] == 0:
        ##좌상단, 위쪽, 왼쪽 셋 중 하나라도 0이라면 넴모가 들어갈 수 있음
        ## 이렇게 보는 이유가 저 ary를 하나씩 더 크게 만든 이유임
        ary[x][y] = 1
        dfs(nx, ny) ## 다음꺼보기
        ary[x][y] = 0

dfs(1,1)



print(cnt)