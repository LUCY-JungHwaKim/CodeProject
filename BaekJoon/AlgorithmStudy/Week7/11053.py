import sys

N = int(sys.stdin.readline())

N_ary = list(map(int, sys.stdin.readline().split()))

dp =[0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if N_ary[i] > N_ary[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))

