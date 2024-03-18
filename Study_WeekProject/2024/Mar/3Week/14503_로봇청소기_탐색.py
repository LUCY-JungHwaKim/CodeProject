import sys
from collections import deque


def bfs():
    mvcnt = 0  ## 청소한 칸의 개수

    while rbq:
        # print(rbq)
        x, y, d = rbq.popleft()

        if ary[x][y] == 0:  ## 청소 되지 않은 경우 청소하기
            ary[x][y] = 2
            mvcnt += 1

        clcnt = 0  ## 청소 칸 카운팅

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < n and 0 <= cy < m and ary[cx][cy] == 0:  ## 청소되지 않은 빈칸 세아리기
                clcnt += 1

        if clcnt == 0:  ## 청소되지 않은 빈 칸이 없는 경우
            newdir = returndic[d]  ## 북쪽이라면 남쪽으로 후진할 수 있도록

            newx = x + dx[newdir]
            newy = y + dy[newdir]

            if 0 <= newx < n and 0 <= newy < m:  ## 범위내에 있고
                if ary[newx][newy] == 2:  ## 후진 가능한 칸 , 청소는 다 되어 있는데 벽이 아닌 경우??
                    rbq.append((newx, newy, d))  ## 후진 할 수 있다면, 바라보는 방향 유지한 채로 후진하고, 1번으로 돌아감
                    continue
                elif ary[newx][newy] == 1:  ## 벽이라면?
                    return mvcnt  ## 작동 멈추기
        else:  ## 청소되지 않은 빈 칸이 있는 경우

            newdir = deque(rcirdic[d])  ## 반시계 방향 회전

            while True:  ## 빈칸 찾을 때까지 회전

                newdir.rotate(1)
                curd = newdir[0]  ## 한바퀴돌리고

                newx = x + dx[curd]
                newy = y + dy[curd]

                if 0 <= newx < n and 0 <= newy < m:
                    if ary[newx][newy] == 0:  ##청소되지 않은 빈 칸인 경우 한칸 전진
                        rbq.append((newx, newy, curd))
                        break
                    else:
                        continue

        # for i in range(n):
        #     print(*ary[i])

    return mvcnt


if __name__ == "__main__":

    ## 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    returndic = [2, 3, 0, 1]  ## 후진할 때의 방향
    # rcirdic = [3, 0, 1, 2] ## 반시계 방향으로 회전할 떄의 방향

    rcirdic = {0: [0, 1, 2, 3], 1: [1, 2, 3, 0], 2: [2, 3, 0, 1], 3: [3, 0, 1, 2]}
    ## rotate 1하면 될것같긴해

    ary = []

    n, m = map(int, sys.stdin.readline().split())

    r, c, d = map(int, sys.stdin.readline().split())

    rbq = deque()  ##로봇큐
    ## 로봇의 위치와 이동하려는 방향

    ## 맵 입력받기
    for _ in range(n):
        ary.append(list(map(int, sys.stdin.readline().split())))

    ## 현재 칸이 청소 되어 있지 않으면 청소 해줌, 근데 로봇이 있는 칸은 항상 빈칸이긴 해 (0이라는 뜻)
    ## 혹시 모르니 방문 배열 만들기

    visited = [[0 for _ in range(m)] for _ in range(n)]

    # ary[r][c] = 2 ## 청소 시켜줌
    # visited[r][c] = 1
    rbq.append((r, c, d))  ## 현재 위치 큐에 넣어주기

    print(bfs())  ## 네방향 탐색
