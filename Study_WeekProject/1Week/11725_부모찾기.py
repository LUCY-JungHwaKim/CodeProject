import sys
n = int(input()) #sys.stdin.readline()
sys.setrecursionlimit(10**5)
## 재귀를 쓰는 경우에는 해당 코드가 필수라고 함
## 재귀의 깊이 제한을 설정하는 코드임

graph = [[] for _ in range(n+1)]
rot = [0 for _ in range(n+1)]
visited = [False] * (n+1)

#print(graph)
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    ## 서로 연결된 거니깐 값 추가해줘야함

#print(graph)



def dfs(graph, start, visited):
    visited[start] = True

    #print(start, end = '')

    for v in graph[start]:
        if not visited[v]:
            rot[v] = start
            ## 여기가 포인트 !!
            ## start가 부모일 것이므로, v인덱스 위치에 start값을 넣어줌
            dfs(graph, v, visited)

dfs(graph, 1, visited)

for m in range(2,n+1):
    print(rot[m])
