from collections import deque

N, K = map(int, input().split())

visited = [-1 for _ in range(100001)]
road = [-1 for _ in range(100001)]
visited[N] = 0

q = deque()

q.append(N)

while q:
    curn = q.popleft()

    if curn == K:
        print(visited[K])
        break

    if 0 <= curn * 2 < 100001 and visited[curn * 2] == -1:
        visited[curn * 2] = visited[curn] + 1
        road[curn * 2] = curn
        q.append(curn * 2)

    if 0 <= curn - 1 < 100001 and visited[curn - 1] == -1:
        visited[curn - 1] = visited[curn] + 1
        road[curn - 1] = curn
        q.append(curn - 1)

    if 0 <= curn + 1 < 100001 and visited[curn + 1] == -1:
        visited[curn + 1] = visited[curn] + 1
        road[curn + 1] = curn
        q.append(curn + 1)

path = []

end = K
while end != N:
    path.append(end)
    end = road[end]
path.append(N)
print(' '.join(map(str, path[::-1])))