from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def bfs_queue(graph, start):
    visited = {}
    queue = deque() #dfs랑 비슷하지만 deque모듈 사용

    queue.append(start) #여기서는 첫번째 방문하는 루트 노드를 방문 리스트에 삽입하지않음
    #이유는 dfs와 bfs 모두 while문 들어가기전에 루트를 visited리스트에 삽입하면 그 다음 노드로 향하지를 않음
    #while문이 종료되는 오류 발생
    
    while queue:
        current = queue.popleft()
        
        if current not in visited:
            visited[current] = True
            queue.extend(graph[current])

    return list(visited.keys())

    

print(bfs_queue(graph, 'A'))

