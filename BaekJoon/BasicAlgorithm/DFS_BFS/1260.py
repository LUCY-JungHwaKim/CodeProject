from collections import deque


dfs_visited = {}
def dfs_recursive(graph, start):
    if start in dfs_visited:
        return
    
    dfs_visited[start] = True
    print(start, end = ' ')
    for current in graph[start]:
        dfs_recursive(graph, current)

bfs_visited = {}
def bfs_search(graph, start):
    
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        if current not in bfs_visited:
            
            print(current, end = ' ')
            bfs_visited[current] = True #여기 안에는 다 current 관련임,, 코드 조심하기
            queue.extend(graph[current])

    return list(bfs_visited.keys())


n,m,v = map(int, input().split())
graph = [ [] for i in range(n+1)]    # 인접 리스트 만들기
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

dfs_recursive(graph, v)
print()
bfs_search(graph, v)

