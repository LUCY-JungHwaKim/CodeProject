n,m = map(int, input().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + ary[i-1][j-1]

## 쉬움 이동방향을 반대로 생각해서
## 인쪽, 위, ㅇ좌상단 대각선에 저장된 dp값들이 그 인덱스까지의 경로 중에서
## 최대 값을 저장한거고, 그거를 현재 인덱스의 값이랑 더하면됨
print(dp[n][m])