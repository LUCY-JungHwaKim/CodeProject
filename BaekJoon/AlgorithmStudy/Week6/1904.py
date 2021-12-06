import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N)]

if N == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 2

    for i in range(2,N):
        dp[i] = (dp[i-2] + dp[i-1])%15746   
        #마지막에 mod 연산을 취하면 더 많은 시간이 걸리기 때문에
        #애초에 dp배열에 넣기전에 mod 연산을 해주는것이 더 적게 소모됨

    print(dp[N-1])