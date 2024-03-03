n = int(input())

for _ in range(n):
    k = int(input())
    ary = list(map(int, input().split()))

    dp = [0 for _ in range(k)]
    #nummax = max(ary)
    dp[0] = ary[0]
    for i in range(1, k):
        dp[i] = max(ary[i] + dp[i - 1], ary[i])

        # print(dp)

    print(max(dp))