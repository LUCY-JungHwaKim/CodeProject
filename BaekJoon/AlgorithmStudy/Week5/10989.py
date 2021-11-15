import sys
T = int(sys.stdin.readline())

N_ary = [0] * 10001

for i in range(T):
    N_ary[int(sys.stdin.readline())] += 1

for i in range(10001):
    if N_ary[i] != 0:
        for j in range(N_ary[i]):
            print(i)
