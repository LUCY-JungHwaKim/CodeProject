from collections import deque


def findtree(x, y):
    cnt = 0
    for i in range(len(dx)):
        cx = x + dx[i]
        cy = y + dy[i]

        if 0 <= cx < n and 0 <= cy < n and ary[cx][cy] > 0 and locs[cx][cy] == 0:  ## 나무가 있는 수만큼 카운팅
            cnt += 1
    return cnt


def plustree(treeq):
    plussvale = deque()
    for x, y in treeq:
        blankcnt = 0  ## 인접칸 중 빈 칸 확인
        dirway = [False, False, False, False]
        for i in range(len(dx)):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < n and 0 <= cy < n and ary[cx][cy] == 0 and locs[cx][
                cy] == 0:  ## 만약 인접칸이 빈칸이고, 범위 내에 있다면 빈칸 수 카운팅
                ## 제초제도 안 뿌려져 있다면
                blankcnt += 1
                dirway[i] = True  ## 그리고 해당 방향 True로 변경
        plussvale.append([x, y, dirway, blankcnt])  ## 큐에 삽입

    # print(plussvale)

    ## 번식 시작
    curtree = []  ## 원래 나무 + 번식된 나무 위치 저장용
    curnum = 0
    while plussvale:
        x, y, dirway, blankcnt = plussvale.popleft()
        curtree.append((x, y))

        if blankcnt != 0:
            curnum = ary[x][y] // blankcnt
            if curnum != 0:  ## 나무가 번식할 수 없을 떄(?)
                for i in range(4):
                    if dirway[i] == True:
                        ary[x + dx[i]][y + dy[i]] += curnum
                        curtree.append((x + dx[i], y + dy[i]))

    curtree = list(set(curtree))  ## 근데 이 부분 좀 터질 수 있음... 왜냐면  set 써서 중복 제거하니깐 나중에 시간초과 되면 이부분 고려하기
    curtree.sort(key=lambda x: (x[0], x[1]))

    return curtree


def chkrmcnt(curtreelst):
    rmary = [[0 for _ in range(n)] for _ in range(n)]  ## 제초제 뿌렷을 때 삭제되는 나무수 저장하는 배열
    ## k : 제초제 확산범위
    maxrmcnt = -9999  ## 제초제를 뿌렸을 때, 가장 많은 나무를 제거하는 위치를 반영해야함
    tmprmcnt = -9999
    tmpx, tmpy = -1, -1
    max_x, max_y = -1, -1
    rsltloc = []

    for i in range(len(curtreelst)):  ## 나무별 탐색할때마다 갱신
        waychk = [False, False, False, False]  ## 벽이나, 나무가 없는 칸을 만났을 시 그 대각선 방향으로는 탐색 그만
        ## True이면 그 대각선방향으로 막힌거지
        rmcnt = 0  ## 제거되는 나무의 수
        grelst = []  ## 제초제 두는 곳 표시

        if sum(waychk) != 4:  ## 네 대각선 방향이 모두 막힌게 아니라면
            for kdx in range(k):  ## k번반복
                for m in range(4):  ## 4방향 대각선 탐색
                    if waychk[m] == False:  ## 그 방향으로 간다면
                        nx = curtreelst[i][0] + (crx[m] * (kdx + 1))
                        ny = curtreelst[i][1] + (cry[m] * (kdx + 1))

                        # print(curtreelst[i][0], curtreelst[i][1], nx, ny,crx[m]*(kdx+1), crx[m]*(kdx+1))
                        if 0 <= nx < n and 0 <= ny < n:
                            if ary[nx][ny] > 0 and locs[nx][ny] == 0:
                                ## 제초제가 안뿌려져 있고, 나무가 있다면
                                rmcnt += ary[nx][ny]
                                # grelst.append((nx, ny))
                            elif ary[nx][ny] <= 0:  ## 막혔으니깐 그쪽으로 아예 안감
                                waychk[m] = True
                            grelst.append((nx, ny))  ## 근데 제초제 위치에는 추가되는거 맞음
                            # elif locs[nx][ny] != 0: ## 제초제가 뿌려져 있으면 그냥 넣기??
                            #     grelst.append((nx, ny))

        rmcnt += ary[curtreelst[i][0]][curtreelst[i][1]]
        grelst.append((curtreelst[i][0], curtreelst[i][1]))

        rmary[curtreelst[i][0]][curtreelst[i][1]] += rmcnt

        # rsltloc = grelst.copy()
        compval = rmary[curtreelst[i][0]][curtreelst[i][1]]  ## 비교할 값
        # print(compval)
        if maxrmcnt < compval:  ## 값이 갱신 될 때만...?
            maxrmcnt = compval
            max_x, max_y = curtreelst[i][0], curtreelst[i][1]
            rsltloc = grelst.copy()

    # print(rmary[max_x][max_y])
    totalrmcnt = rmary[max_x][max_y]

    return max_x, max_y, rsltloc, totalrmcnt


def inpgreen(c, rsltgre, locs):
    ## 2차원 배열에 잡초 뿌려진 년수 넣기

    for i in range(len(rsltgre)):
        ax = rsltgre[i][0]
        ay = rsltgre[i][1]

        locs[ax][ay] = c  ## 제초제뿌린거 설정
        if ary[ax][ay] > 0:  ## 벽은 벽 그대로..
            ary[ax][ay] = 0  ## 제초제 뿌린곳에 0으로 바꿔주긴 해야하네, 나무가 없으니깐


def removegreen():
    for i in range(n):
        for j in range(n):
            if locs[i][j] > 0:
                locs[i][j] -= 1  ## 제초제 년수 1년 깎아주기


if __name__ == "__main__":
    n, m, k, c = map(int, input().split())
    ## 격자의 크기, 박멸이 진행되는 수, 제초제 확산범위, 제초제가 남아있는 년수
    greq = []  ## 연 횟수, 제초제 위치 리스트, 중심값, c
    ary = []

    for _ in range(n):  ## 나무입력 , -1 : 벽
        ary.append(list(map(int, input().split())))

    midx, cidx = 1, 0  ## 현재 몇년차인지, 제초제 연수
    locs = [[0 for _ in range(n)] for _ in range(n)]  ## 제초제 위치에 연수 기록하기 위한것
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    crx = [-1, 1, -1, 1]  ## 대각선방향
    cry = [-1, -1, 1, 1]

    finrmcnt = 0

    for totalcnt in range(m):

        ## 0. 현재 나무 위치를 큐에 저장
        treeq = deque()  ## 나무 위치 저장하는 큐
        for i in range(n):
            for j in range(n):
                if ary[i][j] > 0:
                    treeq.append([i, j])

        ## 1. 인접한 칸 들 중, 나무가 있는 수만큼 성장함
        for x, y in treeq:
            treecnt = findtree(x, y)
            ary[x][y] += treecnt

        ## 2.나무 번식하기, 주위에 빈칸이 세칸이면 현재 나무 성장 수 / 세칸 값을  인접칸의 빈칸 채우기
        curtreelst = plustree(treeq)  ## 나무 번식

        grex, grey, rsltgre, rmtrcnt = chkrmcnt(curtreelst)  ## 제초제를 각 칸에 뿌렸을 시 삭제되는 나무 수 카운팅
        ## 가장 많은 나무를 삭제 시키는 위치 반환

        finrmcnt += rmtrcnt

        ## 제초제를 뿌린 위치 값에 년수를 넣어주기 - 새로운 2차원 배열 생성
        if totalcnt >= 1:  ## 처음 제초제가 심어진 이후
            removegreen()  ## 제초제 연수 깎아주기

        inpgreen(c, rsltgre, locs)  ## 잡초제 뿌린 위치에 연수가 들어간 리스트 반환

        # for i in range(n):
        #     print(*locs[i])

        ## 이 제초제가 전체 연차수가 2년 째일 때, 1년차때 정해진 제초제가 1년차가 되는 거임

        ## ============================================
        ## 여기 위에까지가 1년의 과정임, 제초제는 c년만큼 유지됨
        ## 연 횟수, 제초제 위치 리스트, 중심값, c

        # print(locs)

    print(finrmcnt)