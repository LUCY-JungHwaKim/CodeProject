import sys
sys.setrecursionlimit(1003)

n = int(input())

d = [0 for _ in range(n+1)]
## 초기값 설정
# d[1] = 1
# d[2] = 2


if n == 1:
    d[1] = 1
if n == 2:
    d[1] = 1
    d[2] = 3
if n >= 3:
    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = 2*d[i-2] + d[i-1]

## 다른 코드
# d[1] = 1
# if n >= 2:
#     d[2] = 2
#     for i in range(3, n+1):
#         d[i] = 2 * d[i - 2] + d[i - 1]

rsult = int(d[n] % 10007)
#print(d)
print(rsult)