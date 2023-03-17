graph = [
    [],      # 0
    [2, 3],  # 1
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]

def dfs_stack(graph, start):
    visited = []
    stack = []

    stack.append(start)

    print(stack)

    while stack:
        print(stack)
        now = stack.pop()
        print(now)
        if now not in visited:
            visited.append(now)
            stack.extend(graph[now])
    print(visited)
    return ' '.join(visited)

print(dfs_stack(graph, 1))

visited = []
def dfs_recur(graph, start):
    if start in visited:
        print('done')
        return

    visited.append(start)

    for now in graph[start]:
        dfs_recur(graph, now)

from collections import deque
def bfs(graph, start):

    queue = deque()
    visited = []

    queue.append(start)

    while queue:
        now = queue.popleft()

        if now not in visited:
            visited.append(now)
            queue.extend(graph[now])