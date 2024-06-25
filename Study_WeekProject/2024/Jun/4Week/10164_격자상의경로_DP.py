import sys

if __name__ == "__main__":

    n, m, k = map(int, input().split())

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    ## 0,0 부터 시작하니깐... x,y 둘다 0 이아니라면 거기까지 dp 작업 실행하고
    ## 만약 x,y가 0,0이라면 n,m 까지 작업 실행하기..

    if k == 0:  # 중간에 멈추는거 없이  dp 계산

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp[n][m])
    else:

        x = (k // m) + 1
        y = (k % m)

        if y == 0:
            x -= 1
            y = m

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        rslt = dp[x][y]  ## 중간에 한번 끊기

        dp[x][y] = 1

        for i in range(x, n + 1):
            for j in range(y, m + 1):
                if i == x and y == j:
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(rslt * dp[n][m])