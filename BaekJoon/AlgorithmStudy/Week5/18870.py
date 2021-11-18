import sys

T = int(sys.stdin.readline())

N_ary = list(map(int, sys.stdin.readline().split()))
sorted_ary = sorted(list(set(N_ary)))
dict_ary = {}
for idx, value in enumerate(sorted_ary):    #list.index하면 시간복잡도가 N^2라고함
    dict_ary[value] = idx

for i in N_ary:
    print(dict_ary[i], end=" ")
