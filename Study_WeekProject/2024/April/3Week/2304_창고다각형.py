N = int(input())

ary = [0 for _ in range(1001)]
max_num = 0
max_idx = 0
last_idx = 0
for _ in range(N):
    a,b = map(int, input().split())
    ary[a] = b
    if max_num <= b:
        max_num = b
        max_idx = a
    if a >= last_idx:
        last_idx = a

#print(ary)


#print(max_num, max_idx)
## 왼쪼개 그룹
rsltsum = 0
max_px = 0
for i in range(max_idx+1):
    max_px = max(max_px, ary[i])
    #print(ary[i])
    rsltsum += max_px

## 오른쪽 그룹
max_ax = 0
# print("hell")
# print(last_idx)
for i in range(last_idx, max_idx, -1):
    #print(i)
    max_ax = max(max_ax, ary[i])
    rsltsum += max_ax
print(rsltsum)