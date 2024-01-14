n = int(input())

ary = list(map(int, input().split()))
rsltn = int(input())

avgn = sum(ary) // n

ary = sorted(ary, reverse=False) ## 오름차순 정렬
## 맨 뒤에 있는게 제일 큰거
l,r = 0, ary[-1] ## 시작점을 0으로 해야함

max_num = -99999

while l <= r:
    mid = (l+r) // 2

    totalsum = 0

    for i in range(n):
        if ary[i] <= mid:
            totalsum += ary[i]
        else:
            totalsum += mid

    #print(totalsum, l, mid, r)

    if totalsum > rsltn:
        r = mid - 1
    else:
        l = mid + 1

    #print(l,mid,r)

print(r)