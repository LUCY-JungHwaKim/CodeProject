from collections import deque


def bfs(q):
    cnt = 0
    finlst = []

    while q:
        curlst = q.popleft()

        if curlst[0][0] == nendx and curlst[0][1] == nendy:
            return cnt

        for x in range(4):  ## 4방향 한번에 탐색
            checkFlag = [False] * len(curlst)  ## 움직이는 좌표 움직임 가능성 체크
            ## 만약 해당 값이 모두 True라면 반복문 탈출
            nlst = []
            for i in range(len(curlst)):
                nx, ny = curlst[i][0] + dx[x], curlst[i][1] + dy[x]

                if 0 <= nx < n and 0 <= ny < m and mapary[nx][ny] == 0:  ## 방문하지 않았고, 장애물이 아닌 경우
                    # print("hehl")
                    checkFlag[i] = True
                    nlst.append((nx, ny))
                    # print(checkFlag)

            if sum(checkFlag) == len(curlst):  ## 모두 갈 수 있는 방향이라면?
                q.append(nlst)
                # print("메레레렌")
                # print(curlst, nlst)
                for am in range(len(curlst)):
                    visitx, visity = curlst[am][0], curlst[am][1]
                    mapary[visitx][visity] = 1
                    ### 움직이는 곳 좌표는 다시 0으로 바꿔주기
                for am in range(len(nlst)):
                    movex, movey = nlst[am][0], nlst[am][1]
                    mapary[movex][movey] = 0
                    # print(movex, movey)
            else:
                continue

        # if cnt == 3:
        #     break

        cnt += 1

    return -1


if __name__ == "__main__":

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m, a, b, k = map(int, input().split())

    mapary = [[0 for _ in range(m)] for _ in range(n)]

    stone_ary = []

    for _ in range(k):
        x, y = map(int, input().split())
        mapary[x - 1][y - 1] = 2  ## 장애물 표시
        stone_ary.append((x, y))

    stx, sty = map(int, input().split())
    endx, endy = map(int, input().split())
    nstx, nsty = stx - 1, sty - 1
    nendx, nendy = endx - 1, endy - 1

    ## 위에 변수 네개는 진짜 시작점 끝점 좌표를 저장하기 위한 것임
    ## 시작과 끝점 모두, 사각혀으이 좌상단 좌표임
    ## 사각형 표시는 1로 하기
    stx -= 1
    sty -= 1
    endx -= 1
    endy -= 1
    q = deque()  ## 덱 선언
    stlst = []
    for i in range(a):
        for j in range(b):
            if stx < 0 or sty <0 or endx <0 or endy<0 or stx+i >= n or sty+j >= m or endx+i >= n or endy + j >= m:
                print(-1)
                exit()
            if mapary[stx+i][sty+j] == 2 or mapary[endx+i][endy+j] == 2:  ### 이미 장애물로 표시가 되어 있다면?
                print(-1)
                exit()
            stlst.append((stx+i, sty+j))

    q.append(stlst)

    # for x in range(n):
    #     print(*mapary[x])

    # print(q)

    # finary, finum = bfs(q)
    # if finary:
    #     print(finum)
    # else:  ## 갈수 없는 경우
    #     print(-1)
    finum = bfs(q)

    print(finum)

    ## 위에서 