import sys

n, m = map(int, sys.stdin.readline().split())
ary = []
for _ in range(n):
    ary.append(list(map(int, sys.stdin.readline().split())))

k = int(sys.stdin.readline())  ## 경우의수
recary = []  ## 직사각형 배열

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    recary.append((x1, y1, x2, y2))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  ## 0이 가로합, 1이 세로 합

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1:
            dp[i][j] = dp[i][j - 1] + ary[i - 1][j - 1]
            continue
        if j == 1:
            dp[i][j] = dp[i - 1][j] + ary[i - 1][j - 1]
            continue

        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + ary[i - 1][j - 1]
        ## ary는 1,1 부터 시작이 아니니깐 -1씩 해줘야 하는게 맞음        

# print(dp)

rslt = []

for i in range(k):
    x1, y1, x2, y2 = recary[i][0], recary[i][1], recary[i][2], recary[i][3]
    minx = min(x1, x2) - 1
    miny = min(y1, y2) - 1

    currslt = dp[x2][y2] - dp[minx][y2] - dp[x2][miny] + dp[x1 - 1][y1 - 1]

    # print(x1, y1, x2, y2, minx, miny)
    print(currslt)
