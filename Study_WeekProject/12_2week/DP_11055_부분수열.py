n = int(input())
ary = list(map(int, input().split()))
d = ary.copy() ## 요렇게 해줘야함
#d[0] = ary[0]
for i in range(1, n):
    for j in range(0,i):
        if ary[j] < ary[i]:
            d[i] = max(d[i], ary[i] + d[j])
#print(d)
print(max(d))