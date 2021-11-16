N = list(str(input()))
N = list(map(int, N))

N = sorted(N)


for i in range(len(N)-1, -1, -1):
    print(N[i], end="")