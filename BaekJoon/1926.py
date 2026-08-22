# 백준 1926번 - 그림
import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

count = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            count += 1
            max_size = max(max_size, bfs(i, j))

print(count)
print(max_size)
