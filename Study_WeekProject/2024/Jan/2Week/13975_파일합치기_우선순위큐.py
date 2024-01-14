import heapq
n = int(input())
##heapq 어려워

for _ in range(n):
    m = int(input())

    ary = list(map(int, input().split()))

    rslt = 0

    q = []

    for i in ary:
        heapq.heappush(q,i)
    #print(q)
    while len(q) > 1: ##heapq에 하나만 남을 때까지
        a = heapq.heappop(q)
        b = heapq.heappop(q)

        rslt += a+b

        heapq.heappush(q, a+b)

    print(rslt)