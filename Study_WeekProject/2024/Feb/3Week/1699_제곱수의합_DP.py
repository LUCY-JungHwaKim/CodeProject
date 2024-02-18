n = int(input())


dp = [i for i in range(n+1)] ### 초기화

## 만약 idxr가 7 이면 이보다 작은수의 제곱 dp 값에 1을 더해줌

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i: ## 제곱수가 현재 수보다 크다면
            break
        if dp[i] > dp[i- j*j] + 1: ##최소값이 있다면
            dp[i] = dp[i-j*j] + 1

print(dp[n])