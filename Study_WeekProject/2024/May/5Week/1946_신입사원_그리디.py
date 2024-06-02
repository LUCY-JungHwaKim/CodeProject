T = int(input())

for _ in range(T):

    n = int(input())

    ary = []

    for _ in range(n):
        a,b = map(int, input().split())

        ary.append((a,b))


    ary.sort(key = lambda x : x[0])

    curn, curm  = ary[0][0], ary[0][1]
    ## 현재 서류심사 성적, 면접 성적 순위임!! 그래서 작은게 더 높윽너임

    cnt =  1
    for i in range(1, n):
        if ary[i][0] < curn or ary[i][1] < curm:
            curn = ary[i][0]
            curm = ary[i][1]
            cnt += 1

        else:
            continue

    print(cnt)