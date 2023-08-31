import heapq
import sys

INF = int(1e9) ## 무한의 값

n,m = map(int, sys.stdin.readline().split())
## 노드, 간선 개수

start = int(input())

graph = [[] for i in range(n+1)]
## 노드 정보 리스트

distance = [INF] * (n+1)
## 최단 거리 테이블

for _ in range(m):
    ## 모든 간선 정보 입력
    a,b,c  = map(int, sys.stdin.readline().split())

    graph[a].append((b,c))
    # a번에서 b번 노드로 가는 비용이 c라는 의미

def dijkstra(start):
    # 다익스트라, 힙큐사용

    q = []

    heapq.heappush(q, (0, start))
    ## 먼저 제일 첫번째 ! 시작노드로 가기위한 최단 경로는 0이므로 이를 큐에 삽입

    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)
        ## 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist:
            ## 이미 처리된 적이 있는 노드라면 무시
            ## 그러니까 distance리스트에 있는 값이 더 작으면 갱신안해도 됨
            continue

        for i in graph[now]:
            ## 인접한 노드 확인

            ## 다음 노드로 이동하는 거리 계산
            cost = dist + i[1] ## 여기서 1인 이유는 위에서 c라는 비용 값이 튜플에서 두번째 요소이기 때문

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) ## 거리 노드 새로 삽입

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    ## 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
