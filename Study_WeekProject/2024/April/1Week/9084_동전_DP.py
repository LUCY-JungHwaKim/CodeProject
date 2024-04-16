import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    finum = int(sys.stdin.readline())

    dp = [0] * (finum + 1)

    dp[0] = 1  ## 초기값을 이렇게 둬야 뒤에 점화식 계산이 가능한듯
    ## 어렵네

    for coin in coins:
        for i in range(1, finum + 1):
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[finum])

### 어려웡 힝 https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-9084-%EB%8F%99%EC%A0%84-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC

