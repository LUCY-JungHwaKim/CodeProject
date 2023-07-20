
def dfs(graph, v, visited):

    visited[v] = True ## 먼저, 해당 노드 방문 확인
    print(v, end = ' ')
    for i in graph[v]: # 노드와 연관된 다른 노드들 확인
        if not visited[i]: # 방문하지 않았다면
            dfs(graph, i, visited) # 재귀 함수 실행



graph = [
    [],
    [2,3,8], # 1의 노드에는 2,3,8이 달려있다는 뜻
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 ## 방문 여부 리스트

dfs(graph,1, visited)

