from collections import deque
n,m = map(int, input().split())

graph = []
for i in range(n): ## 이미 여기서 stack, list 만든거임
    graph.append(list(map(int, input()))) ## split을 안하면 입력할때 띄어쓰기로 입력 안해도 됨

## bfs : queue
## dfs : stack, 재귀

print(graph)

dx = [-1, 1, 0,0] ## 상하좌우
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append((x,y))


    while q:

        x,y = q.popleft()

        for i in range(4): ## 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0: ## 크기 벗어나는지 확인
                continue

            if graph[nx][ny] == 0: ## 괴물 유무 확인
                continue

            if graph[nx][ny] == 1: ## 괴물이 없다면?
                graph[nx][ny] = graph[x][y] + 1 ## 해당좌표값 +1

                q.append((nx,ny)) ## 큐에 이동한 좌표 새로 삽입

    return graph[n-1][m-1] ## 마지막 좌표 값 출력 = 움직인 칸의 개수

print(bfs(0,0))

