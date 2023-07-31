from collections import deque

def bfs(graph, v, visited):

    q = deque([v])
    
    visited[v] = True # 현재 노드 방문 처리
    
    while q: ## queue가 빌 떄 까지 반복
        p = q.popleft() ## 하나 먼저 뽑고
        
        for i in graph[p]:
            if not visited[i]: ## 방문하지 않았다면 
                q.append(i) # 큐에 삽입하고
                visited[i] = True # 방문 처리
                



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

bfs(graph,1, visited)


## 확인ㅇ용
# #
# def dfs(graph, start, visited):
#     q = deque([start])
#
#     visited[start] = True
#
#     while q:
#         p = q.popleft()
#
#         for i in graph[p]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True