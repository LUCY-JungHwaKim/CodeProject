import sys

sys.setrecursionlimit(10000)
n = int(input())
## 그래프로 풀어야 함

ary = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    ary[int(input())].append(i)

rslt = []


# ans = set()

def dfs(v, i):
    visited[v] = True

    for k in ary[v]:
        if not visited[k]:
            dfs(k, i)

        elif visited[k] and k == i:
            rslt.append(k)


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)  ## startn, n

print(len(rslt))
for i in rslt:
    print(i)

# https://yuna0125.tistory.com/182?category=1271911