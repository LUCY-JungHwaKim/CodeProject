n = int(input())

ary = [[0, 0] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    ary[i + 1][0], ary[i + 1][1] = a, b
# print(ary)
k = int(input())

dp = [[0, 0] for _ in range(n + 1)]
## 최대 점프 때문에 두개 만들어줘야함!
## 첫번째는 최대점프 안할 때, 두번째는 최대점프 할 떄!


jumpflag = 0  # 매우 큰 점프는 한번만 할 수 있댔음

if n >= 2:
    dp[2][0] = ary[1][0]

if n >= 3:
    dp[2][0] = ary[1][0]
    dp[3][0] = min(dp[2][0] + ary[2][0], ary[1][1])
## 썼다 안썼다 하는 경우를 확인해봐야할것같음...

if n >= 4: ## 4이상인 것부터 매우 큰 점프를 할 수 있음
    for i in range(4, n + 1):

        dp[i][0] = min(dp[i - 1][0] + ary[i - 1][0], dp[i - 2][0] + ary[i - 2][1]) ## 큰 점프 안할때
        
        ## 큰 점프 할 때, i마다 다름
        if i == 4:
            dp[i][1] = k
        elif i == 5:
            dp[i][1] = min(dp[i - 3][0] + k, ary[i-1][0] + k)
        else:
            dp[i][1] = min(dp[i-3][0]+k, dp[i-4][0] + k + ary[i-1][0], dp[i-5][0] + k + ary[i-2][1])
# print(dp)
if n <= 3:
    print(dp[n][0])
else:
    print(min(dp[n][0], dp[n][1]))