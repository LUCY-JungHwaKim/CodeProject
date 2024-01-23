n = int(input())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))


dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = 1

# def caldp(dp, ary, x, y):


#     if (x + ary[x][y] < n):
#         dp[x+ary[x][y]][y] = max(dp[x+ary[x][y]][y], dp[x][y] + 1)

#     if (y+ary[x][y] < n):
#         dp[x][y+ary[x][y]] = max(dp[x][y+ary[x][y]], dp[x][y])

##dp로 잘 생각했는데, 조금 더 생각했어야 했다 
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[n-1][n-1])
            break
        if (i + ary[i][j] < n):
            dp[i + ary[i][j]][j] += dp[i][j]

        if (j + ary[i][j] < n):
            dp[i][j + ary[i][j]] += dp[i][j]