from collections import deque
N,M = map(int, input().split())

S,E = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1) ## 체크 리스트 

for _ in range(M):
    a,b = map(int, input().split())

    graph[a].append(b) ## 쌍방으로 입력
    graph[b].append(a)


def bfs(node):

    q = deque()
    q.append(node)
    visited[node] = 0 ## 먼저 처음 영역 방문 표시

    while q:
        node = q.popleft()

        d = [node-1, node+1] ## 방향 지정

        if graph[node]:
            d += graph[node] ## 옆으로 나란히 붙여주기, 텔레포트를 토앻 가는 곳을
        #print(d)
        for xval in d:
            if 1 <= xval <= N and visited[xval] == -1: ## 만약 갈 수 있다면
                q.append(xval)
                visited[xval] = visited[node] + 1
            if xval == E: ## E에 도착했다면
                return visited[xval]

cnt = bfs(S)
print(cnt)