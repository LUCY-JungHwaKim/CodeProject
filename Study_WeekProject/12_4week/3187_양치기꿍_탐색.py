from collections import deque
n, m = map(int, input().split())
ary = []

for i in range(n):
    ary.append(list(map(str, input())))

dx = [0, 0, 1, -1]  ## 동, 서, 남, 북
dy = [1, -1, 0, 0]


def bfs(graph, x, y):

    q = deque()
    q.append((x,y))

    k_cnt, v_cnt = 0,0

    if graph[x][y] == 'k':
        k_cnt += 1
    elif graph[x][y] == 'v':
        v_cnt += 1

    ary[x][y] = '#'

    while q:

        nx, ny = q.popleft()

        for i in range(len(dx)):
            cx = nx + dx[i]
            cy = ny + dy[i]

            if cx < 0 or cx >=n or cy < 0 or cy >= m:
                continue

            if ary[cx][cy] == '#': ## 울타리라도 패스
                continue
            else:
                if ary[cx][cy] == 'k':
                    k_cnt += 1

                elif ary[cx][cy] == 'v':
                    v_cnt += 1

                ary[cx][cy] = '#'  ## 울타리 설치함
                q.append((cx, cy))

    if k_cnt > v_cnt: # 양이 늑대보다 많을 경우, 늑대가 전부 잡아먹힘
        v_cnt = 0
    else:
        k_cnt = 0

    return k_cnt, v_cnt

fin_k, fin_v = 0,0
for i in range(n):
    for j in range(m):
        if (ary[i][j] == 'k') or (ary[i][j] == 'v'):
            k_cnt, v_cnt = bfs(ary, i, j)
            fin_k += k_cnt
            fin_v += v_cnt

print(fin_k, fin_v)