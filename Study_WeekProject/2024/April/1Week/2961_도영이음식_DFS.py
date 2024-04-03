import sys

n = int(sys.stdin.readline())

ary = []

for _ in range(n):
    ary.append(list(map(int, sys.stdin.readline().split())))


def dfs(sol, idx, depth):
    global minvalue

    mulx, sumx = 1, 0
    for j in range(len(sol)):
        mulx *= sol[j][0]
        sumx += sol[j][1]

        diffx = abs(mulx - sumx)

        minvalue = min(minvalue, diffx)

    if depth == n - 1:
        return

    for i in range(idx, n):
        sol.append(ary[i])
        dfs(sol, i + 1, depth)
        sol.pop()


sol = []
minvalue = 1e+9
for i in range(n):
    sol.append(ary[i])
    dfs(sol, i + 1, i)
    sol.pop()

print(minvalue)