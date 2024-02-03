n,m = map(int, input().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))

loclst = []
for _ in range(m): ## 찾는 구간
    loclst.append(list(map(int, input().split())))

## 먼저 DP 값 부터 구해야함
def calDP():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = ary[0][0]  ## 값 초기화

    for i in range(n):
        for j in range(n):

            if i == 0 and j > 0: ## 일단 첫행 먼저
                dp[i][j] = dp[i][j-1] + ary[i][j]
            if i > 0 and j == 0: ## 첫열
                dp[i][j] = dp[i-1][j] + ary[i][j]
            if i > 0 and j > 0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + ary[i][j]
    return dp

def findCnt(dp,x1, y1, x2, y2):

    if x1 == 0 and y1 > 0: ## 첫 행에서 시작하는 경우
        rslt = dp[x2][y2] - dp[x2][y1-1]
    if y1 == 0 and x1> 0: ## 첫 열에서 시작하는 경우
        rslt = dp[x2][y2] - dp[x1-1][y2]
    if x1 == 0 and y1 == 0: ## 그냥 처음부터 시작할 때
        rslt = dp[x2][y2]
    if x1 == x2 and y1 == y2: ## 서로 같을 때
        rslt = ary[x1][y1]
    if x1 > 0 and y1 > 0: ## 그냥 일반
        rslt = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]

    return rslt


dp = calDP()

for i in range(len(loclst)):
    rslt = findCnt(dp, loclst[i][0]-1,loclst[i][1]-1,  loclst[i][2]-1,  loclst[i][3]-1)
    print(rslt)