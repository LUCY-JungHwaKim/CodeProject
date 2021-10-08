# 1) 스택을 이용한 DFS 구현
def dfs_stack(graph, start):
    visited = []
    stack = []
    
    # 시작 노드 스택에 담기   
    stack.append(start)
    print(stack)
    # 스택에 방문하지 않은 인접 정점들을 담은 후 하나씩 빼오면서 탐색
    while stack:
        print(stack)
        now = stack.pop()
        print(now)
        if now not in visited: 
            visited.append(now)
            stack.extend(graph[now])

    return ' '.join(visited)

# 그래프 탐색 (BFS)
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque()

    # 시작노드 큐에 담기
    queue.append(start)

    # 방문 노드와 연결된 모든 노드들을 담고 하나씩 방문
    while queue:
        # 큐의 맨 앞 노드 빼오기
        now = queue.popleft()
        # 아직 방문하지 않았다면 방문 마크 후 인접 노드들 큐에 넣기
        if now not in visited:
            visited.append(now)
            queue.extend(graph[now])

    return ' '.join(visited)
visited = []
def dfs_recursive(graph, start):
    # 이미 방문한 노드라면 탐색 종료
    if start in visited:
        print(start+"hello")
        return
    
    # 방문 표시
    visited.append(start)
    print(visited)
    print(start, end=' ')

    # 인접 정점들에 대해 재귀 호출
    for now in graph[start]:
        dfs_recursive(graph, now)

graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
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
print(dfs_recursive(graph, 'A'))
#print(dfs_stack(graph, 'A'))  
#print(bfs(graph, 'A'))