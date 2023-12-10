from collections import deque

n = int(input())
ary = list(map(int, input().split()))

## 그냥 이전합까지 계산한거를 현재 숫자랑 더하고, 더 큰 값을 넣으면 됨..
## 나만 어렵게 푼듯..내꺼는 반복문을 두번 돌아야 하니까나 시간 초과 난듯

for i in range(1, n):
    ary[i] = max(ary[i], ary[i] + ary[i-1])

print(max(ary))
# totalary = []
#
# for i in range(n):
#     d = [0 for _ in range(n)]
#     d[i] = ary[i]
#     max_s = d[i]
#     if i < n-1:
#         for j in range(i+1, n):
#             d[j] = d[j-1] + ary[j]
#             if max_s < d[j]:
#                 max_s = d[j]
#
#     else:
#         if max_s < d[i]:
#             max_s = d[i]
#     totalary.append(max_s)
#
# print(max(totalary))