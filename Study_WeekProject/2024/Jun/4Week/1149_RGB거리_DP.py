import sys

if __name__ == "__main__":

    n = int(input())

    ary = []

    for _ in range(n):
        ary.append(list(map(int, input().split())))

    dp = [[0] * 3 for _ in range(n + 1)]
    ## 영역 하나에 대한 최소값 가져오기
    # dp[1] = 99999
    for i in range(3):
        dp[1][i] = ary[0][i]

    for i in range(2, n + 1):
        dp[i][0] = ary[i - 1][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = ary[i - 1][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = ary[i - 1][2] + min(dp[i - 1][0], dp[i - 1][1])

    # 빨,초,파 값을 따로 다 나눠서
    # 현재 값에  현재 선택된 색깔 이외의 색깔들을 이전에 선택했을때의 값들을 다 더해줌
    # 예로 들면 현재 빨을 선택했으면
    # 이전 dp 인덱스의 초록 파랑을 선택한 값중 최소값을 가져오는 거임!

    print(min(dp[n]))