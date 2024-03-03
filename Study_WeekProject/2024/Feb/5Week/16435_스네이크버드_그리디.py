N, L = map(int, input().split())

ary = list(map(int, input().split()))

ary.sort(reverse=False) ## 작은것부터 정렬


for i in range(N):
    if ary[i] <= L:
        L += 1

print(L)
