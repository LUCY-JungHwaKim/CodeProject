
while True:
    n = int(input())

    if n == 0:
        break

    ary = []
    dp = [-99999 for _ in range(n+1)]


    for _ in range(n):
        ary.append(int(input()))
    #print(ary)
    dp[1] = ary[0]

    for i in range(2, n+1):
        dp[i] = max(dp[i-1] + ary[i-1], ary[i-1])
    #print(dp)
    print(max(dp))
    ## dp는 현재 구간별로 처음부터 지금 인덱스까지
    ## 최대값을 가져오는 거임

