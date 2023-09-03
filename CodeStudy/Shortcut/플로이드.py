import heapq
import sys

INF = int(1e9) ## 무한의 값

n = int(input()) ## 노드
m = int(input()) ## 간선


graph = [[INF] * (n+1) for i in range(n+1)]
## 노드 정보 리스트

## 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

## 각 간선값 입력

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

## 점화식 이용해서 플로이드 워셜 알고리즘 수행

for k in range(1, n+1): ## 노드 개수 만큼
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

## 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
    
