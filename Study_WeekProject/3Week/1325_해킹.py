## bfs로 풀어보자
from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int, input().split())

ary = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())

    ary[b].append(a)





def bfs(ary, start):
    visited = [False] * (n + 1)
    cnt  = 1
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()

        for i in ary[cur]:
            if not visited[i]: ## 방문하지 않았다면
                visited[i] = True
                queue.append(i)
                cnt += 1


    return cnt

rsult_ary = []
for i in range(1, n+1):
    rsult_ary.append(bfs(ary, i))

max_n = max(rsult_ary)
for i in range(len(rsult_ary)):
    if rsult_ary[i] == max_n:
        print(i+1, end=" ")