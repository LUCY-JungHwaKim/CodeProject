from collections import deque

N = int(input())

ary = []
for _ in range(N):
    ary.append(list(map(int, input())))

# print(ary)

# 1이 흰방, 0이 검은방
q = deque()
visited = [[0 for _ in range(N)] for _ in range(N)]
weights = [[99999 for _ in range(N)] for _ in range(N)]
q.append((0, 0))
weights[0][0] = 0
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if weights[nx][ny] > weights[cx][cy]:  ## 약간 여기 weights가 몇개의 벽을 뚫어야 한다 그 의미라고 생각하면 될듯?
                    ## 벽이면
                    if ary[nx][ny] == 0:
                        weights[nx][ny] = weights[cx][cy] + 1
                    else:
                        weights[nx][ny] = weights[cx][cy]
                    q.append((nx, ny))


bfs(0, 0)

# for i in range(N):
#     print(*weights[i])

print(weights[N - 1][N - 1])
# https://velog.io/@igun0423/%EB%B0%B1%EC%A4%80-2665-%EB%AF%B8%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0-Python