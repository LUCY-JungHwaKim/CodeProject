T = int(input())

N_ary = []
for i in range(T):
    x,y = map(int, input().split())
    N_ary.append((y,x))

N_ary = sorted(N_ary)
for y,x in N_ary:
    print(x,y)