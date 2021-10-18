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
    #이유는 queue는 FIFO이기 때문에 루트노드가 들어가면 방문했다고 파악하여 탐색을 멈춤
    
    while queue:
        current = queue.popleft()
        
        if current not in visited:
            visited[current] = True
            queue.extend(graph[current])

    return list(visited.keys())

    

print(bfs_queue(graph, 'A'))