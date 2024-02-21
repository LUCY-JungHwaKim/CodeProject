from collections import deque

n, m = map(int, input().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(m):
#         if ary[i][j] == 1: ## 치즈가 있다면
#             q.append((i,j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cntary = []


def bfs():
    q = deque()  ## 치즈 위치 저장..
    q.append((0, 0))
    visited[0][0] = 1
    # firlength = len(queue) ## 처음 들어올때 큐의 길이
    chkcnt = 0

    while q:
        x, y = q.popleft()

        for i in range(len(dx)):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < n and 0 <= cy < m and visited[cx][cy] == 0:  ## 이동하려고 하는 좌표가 범위 안에 있고
                if ary[cx][cy] == 1:  ## 가장자리 카운팅
                    # queue.append((cx,cy))
                    ary[cx][cy] = 0
                    visited[cx][cy] = 1
                    chkcnt += 1
                elif ary[cx][cy] == 0:
                    q.append((cx, cy))
                    visited[cx][cy] = 1

    cntary.append(chkcnt)
    # print(cntary)
    return chkcnt


## 0에서 1로 갈때만 체크해 주기 : 이게 바로 테두리(?)\

totalcnt = 0  ## bfs 실행 횟수
while True:
    totalcnt += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]  ## 모서리용
    cnt = bfs()
    if cnt == 0:
        break

print(totalcnt - 1)
print(cntary[-2])