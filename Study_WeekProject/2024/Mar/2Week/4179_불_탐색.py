
import sys
from collections import deque

def move():

    while True:

        for jidx in range(len(jq)): ## 지훈이 먼저 이둥
            jx,jy = jq.popleft()

            if ary[jx][jy] == 'F':
                continue ## 만약 지훈이 이동할 곳이 불이라면 패스

            for i in range(4):
                jcx = jx + dx[i]
                jcy = jy + dy[i]

                if 0<=jcx<r and 0<=jcy<c: ## 범위 내에 있고
                    if ary[jcx][jcy] == '.': ## 갈수 있는 곳이라면
                        jq.append((jcx, jcy))
                        ary[jcx][jcy] = ary[jx][jy] + 1
                else:## 범위를 벗어나면 탈출 성공
                    return ary[jx][jy] + 1

        ## 불 이동
        for fidx in range(len(fq)):
            fx, fy = fq.popleft()

            for i in range(4):
                fcx = fx + dx[i]
                fcy = fy + dy[i]

                if 0<=fcx<r and 0<=fcy<c:
                    ## 빈곳이거나 지훈이 지나간 곳이면 삽입
                    if ary[fcx][fcy] == '.' or type(ary[fcx][fcy]) == int:
                        fq.append((fcx, fcy))
                        ary[fcx][fcy] = 'F'

        #
        # for i in range(r):
        #     print(*ary[i])

        if not jq: ## 지훈이의 좌표가 없다면
            return "IMPOSSIBLE"


if __name__ == "__main__":
    r, c = map(int, sys.stdin.readline().split())

    ary = []

    for _ in range(r):
        ary.append(list(map(str, sys.stdin.readline().strip())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    jq = deque()
    fq = deque()
    # firex, firey, jxx, jyy = 0,0,0,0
    ## 근데 불이 없을 수 있음, 여러개 일 수도 있음
    ## 지훈이는 1분에 한칸, 불은 1분에 인접한 네 방향에 모두 퍼짐
    ## 불 먼저 퍼뜨리고, 사람이 갈수 있는지 확인


    for i in range(r):
        for j in range(c):
            if ary[i][j] == 'F':
                fq.append((i, j))
            if ary[i][j] == 'J':
                jq.append((i, j))
                ary[i][j] = 0 ## 방문처리


    print(move()) ## 한번에 움직이기