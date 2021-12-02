N = int(input())

# 0 1 2 3 4 5 6 7 8 9
# 자리수(1) 0 1 1 1 1 1 1 1 1 1
# 자리수(2) 1 1 2 2 2 2 2 2 2 1
# 자리수(3) 1 3 3 4 4 4 4 4 3 2
# 왼쪽대각선 위, 오른쪽 대각선 위 를 더하면 해당 자릿수 결과가 나옴
# 이차원 행렬로 문제 풀이

dp = [[0 for i in range(10)] for j in range(N+1)]

for i in range(1,10):
    dp[1][i] = 1

if N >= 2:
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    

print(sum(dp[N])%1000000000)