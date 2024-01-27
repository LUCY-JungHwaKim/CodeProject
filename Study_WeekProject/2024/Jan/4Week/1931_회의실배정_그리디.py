n = int(input())

ary = []
difary = []
## 끝나는 시간이 이른대로 정렬, 만약 끝나는 시간이 같으면
# 빨리 시작하는 순서대로 정렬

for _ in range(n):
    a,b  = map(int, input().split())
    ary.append((a,b))


ary.sort(key = lambda x: (x[1], x[0]))

roomcnt = 1
ends = ary[0][1]

for i in range(1, n):
    if ary[i][0] >= ends:
        ends = ary[i][1] ## 현재 끝나는 시간으로 변경
        roomcnt += 1

print(roomcnt)

## 정렬까지는 갔는데 끝나는 시간으로 젖ㅇ렬해야 되는 줄은 몰ㄹ랐다..