import sys
from collections import deque


def checkwater(iceq):
    while iceq:

        x, y = iceq.popleft()

        visited[x][y] = False

        seacnt = 0
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < n and 0 <= cy < m and ary[cx][cy] == 0:  ## 범위 내에 있고, 바다와 닿아져있다면
                seacnt += 1

        waterary[x][y] = seacnt


def minusbing():
    for i in range(n):
        for j in range(m):

            if ary[i][j] - waterary[i][j] > 0:
                ary[i][j] -= waterary[i][j]
                iceq.append((i, j))
                # chkary[i][j] = 1 ## 이거 굳이 필요 없어보이긴 해
            else:
                ary[i][j] = 0
                # chkary[i][j] = 0

            waterary[i][j] = 0


def countcorpus(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    ## 빙산큥에 위치 넣어주기

    cnt = 0
    while q:
        x, y = q.popleft()

        for idx in range(4):
            cx = x + dx[idx]
            cy = y + dy[idx]

            # print(x,y,cx,cy)

            if 0 <= cx < n and 0 <= cy < m and ary[cx][cy] > 0 and visited[cx][cy] == False:
                # 범위 내에 있고, 빙산이 있고, 방문하지 않은 경우
                q.append((cx, cy))
                visited[cx][cy] = True
                cnt += 1

    return cnt


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    ary = []

    for _ in range(n):
        ary.append(list(map(int, sys.stdin.readline().split())))

    iceq = deque()  ## 빙산 위치 저장 큐

    for i in range(n):
        for j in range(m):
            if ary[i][j] > 0:
                iceq.append((i, j))

    dx = [-1, 1, 0, 0]  ## 네 방향 탐색
    dy = [0, 0, -1, 1]

    yearcnt = 0  ## 연도 카운트, 한해만에 빙하가 녹을땐 0 출력

    visited = [[False for _ in range(m)] for _ in range(n)]
    waterary = [[0 for _ in range(m)] for _ in range(n)]  ## 각 요소별로 물과 맞닿아있는 면적 구하기

    while len(iceq) != 0:

        # ================
        # 1. 네 방향 돌면서 물과 맞닿아있는지 확인

        checkwater(iceq)

        # 2. 빙산 높이에서 맞닿아있는 바다 수만큼 뻬주기

        # for i in range(n):
        #     print(*waterary[i])

        minusbing()  ## 바다 수만큼 빼주기

        # for i in range(n):
        #     print(*ary[i])

        bingcorpus = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and ary[i][j] > 0:  ##빙산이 있고 방문하지 않은 경우만
                    bingcnt = countcorpus(i, j)  ## 빙산 덩어리 수 세는거
                    bingcorpus += 1
        # print(bingcorpus)

        if bingcorpus >= 2:  ## 2덩이 이상일때의 최초년수 출력
            print(yearcnt + 1)
            exit()

        # if bingcorpus == 0: ## 빙하가 다 녹았는데
        #     if yearcnt == 0:
        #         print(0) ## 한해전에 빙하가 모두 녹았으므로
        #         break
        #     else:
        #         print(yearcnt)
        #         break

        yearcnt += 1

        # print(bingcorpus)
        # print(iceq)

    print(0)