import sys

h,w = map(int, sys.stdin.readline().split())

numary = list(map(int, sys.stdin.readline().split()))

ary = [[0 for _ in range(w)] for _ in range(h)]

fir = numary[0]
cnt = 0

for i in range(1, len(numary)-1):
    ## 현재 위치 기준 양옆 맥스값 구하기
    left = max(numary[:i])
    right = max(numary[i+1:])

    diff = min(left, right)

    if numary[i] < diff:
        cnt += (diff - numary[i])

print(cnt)