T = int(input())
N_ary = []
for i in range(T):
    x,y = map(int, input().split())
    N_ary.append((x,y))

N_ary = sorted(N_ary)
for x,y in N_ary:
    print(x,y)