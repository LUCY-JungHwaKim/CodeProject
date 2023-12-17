import heapq

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

INF = int(1e9)
distance = [INF] * (n + 1)


def short_dist(start):
    q = []  # 거리랑 좌표 기록하는거?

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


short_dist(x)
# print(distance)
## x : start
# dis_idx = distance.index(k)
if k not in distance:
    print(-1)
else:
    for i, x in enumerate(distance):
        if x == k:
            print(i)