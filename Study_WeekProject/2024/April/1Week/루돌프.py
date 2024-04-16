from collections import deque

def calDist(santaAry, rx, ry):

    distary = []
    for i in range(len(santaAry)):
        sr = santaAry[i][1]
        sc = santaAry[i][2]
        px = santaAry[i][0]
        dist = (rx-sr)**2 + (ry - sc)**2

        distary.append([dist, px, sr, sc])

    distary.sort(key=lambda x : (x[0], -x[2], -x[3])) ## 가장 까까운거 선택
    # 근데 산타가 2명 이상일수 있으니깐 r,c가 각각 큰 순서대로

    print(distary)

    return distary[0] ## 가장 가까운 산타 값 전달

def moveRudolf(santainf):
    
    ## 현재 루돌프 위치랑 가장 가까운 산타 와의 8방향 중에서 가장 가까운 방향 찾기
    distary = []
    rudolfColFlag = False ## 루돌프가 움직였다는 뜻의 flag
    sanNum = -1 ## 루돌프가 부딪힌 산타 번호
    
    for i in range(len(dx)):
        cx, cy = rx + dx[i], ry + dy[i]
        
        dist = (cx - santainf[2])**2 + (cy - santainf[3])**2
        
        distary.append([dist, cx, cy, i]) ## 이동방향도 같이 넣어주기
    
    distary.sort(key = lambda x : (x[0], -x[1], -x[2]))
    ## 거리가 가깝고, r이나 c가 큰 쪽으로
    
    minx,miny = distary[0][1], distary[0][2] ## 제일 가까운 방향

    if mapary[minx][miny] != 0 : ## 그 자리에 산타가 있었다면? 빈칸이 아니라면?
        rudolfColFlag = True

    mapary[rx][ry] = 0 ## 루돌프가 지나간 자리 표시(원래 없던것으로)
    mapary[minx][miny] = 2 ## 루돌프 표시

    return rudolfColFlag, minx, miny, santainf[1], distary[0][3] ## 루돌프랑 가장 가까운 산타의 번호

def moveSanta():

    curlen = len(santaAry) ## 초기 산타가 들어있던 ary
    collapseFlag, colx, coly, colsan = False, -1, -1, 0
    ## 루돌프랑 산타가 충돌했을때 기록하기 위한 것
    ## 충돌 여부, 충돌 하기 전 산타가 원래 있던 곳 좌표, 그리고 산타 번호

    for i in range(curlen):
        #santanum, cx, cy, score = santaAry.popleft()
        cx, cy = santaAry[i][1], santaAry[i][2]
        #print(santanum, cx, cy, score)
        distary = []
        for j in range(4): ## 산타는 상우하좌 이렇게 네 방향으로만 움직이기 가능함
            nx, ny = cx + dx[j], cy + dy[j]

            if 0<=nx<n and 0<=ny<n: ## 범위 내일때만

                dist = ((nx-rx)**2) + ((ny-ry)**2)
                distary.append([dist, nx, ny, j])

        print(distary)
        if len(distary) > 0: ## 움직일 수 있는 칸이 있다다면
            distary.sort(key=lambda x: (x[0], x[3])) ## j순대로 하면 상우하좌 순임
        else:
            continue
        print(distary)
        finx, finy = distary[0][1], distary[0][2] ## 산타가 이동할 곳


        if 0<=finx<n and 0<=finy<n: ## 범위 내에 있고,
            if mapary[finx][finy] == 0: ## 산타나 루돌프도 없고, 갈수 있는 곳이라면?
                mapary[cx][cy] = 0 ## 산타 자리 지우기
                santaAry[i][1] = finx
                santaAry[i][2] = finy
                mapary[finx][finy] = 1 ## 새로 산타 자리 채우기
            elif mapary[finx][finy] == 2: ## 산타가 루돌프 만나면?
                collapseFlag = True
                colx, coly = cx, cy
                colsan = i
            else: ## 산타를 만나면 현재 자리 유지
                continue


    return collapseFlag, colx, coly, colsan, distary[0][3] ## 충돌했을때의 위치랑 산타이름

def rusanCollapse(colx, coly, colsan, locway, rusanFlag):

    if rusanFlag == "Rudolf": ## 루돌프가 와서 충돌한 경우
        santaAry[colsan][3] += c ## 루돌프가 와서 부딪혔을 때 c만큼 점수 얻기

        nx = colx + (dx[locway]*c)
        ny = coly + (dy[locway]*c)
        ## 산타는 루돌프가 이동해온 방향으로 c칸만큼 밀려나게 됨
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n: ## 범위밖으로 움직인다면?
            ## 산타 탈락됨
            santaScore[colsan] += santaAry[colsan][3] ## 점수 더해주고 탈락하기
            ###############3 Santa ary 에 맨 마지막에 얘가 살았다 죽었다 표시를 해줘야할것같은데
        
        santaAry[colsan][1] = nx
        santaAry[colsan][2] = ny
        
        mapary[nx][ny] = 1 ## 지도에 산타가 있다고 그려주기
    
    else:
        santaAry[colsan][3] += d



if __name__ == "__main__":
    n,m,p,c,d = map(int, input().split())
    ## n: 게임판크기, m : 게임턴수,
    ## p : 산타수, c:루돌프힘, d : 산타 힘
    mapary = [[0 for _ in range(n)] for _ in range(n)]  ## 게임판구성
    rx, ry = map(int, input().split()) ## 루돌프 초기 위치 (-1 해줘야함, 나는 이게 편해)
    rx -= 1
    ry -= 1

    mapary[rx][ry] = 2 ## 루돌프

    santaScore = [0 for _ in range(p)] ## 산타 수만큼
    
    #루돌프가 이동할때의 좌표
    dx = [-1,0,  1, 0, -1, -1, 1, 1 ] #상우하좌
    dy = [0, 1, 0, -1, -1, 1, -1, -1]

    santaAry = []

    for _ in range(p):
        px, sr, sc = map(int, input().split())
        ## 산타 번호, 초기 위치
        santaAry.append([px, sr-1, sc-1, 0, False]) ## 마지막은 산타의 점수, 맨마지막꺼가 False면 아직 살아있는거
        mapary[sr-1][sc-1] = 1 ## 산타표시

    ##루돌프가 움직이고
    ## 1번 산타부터 p번 산타까지 움직이기
    print('[-------------')
    for i in range(n):
        print(*mapary[i])
    
    santaAry.sort(key = lambda x : x[0]) ## 산타 번호대로 정렬
    santaAry = deque(santaAry)


    santainf = calDist(santaAry, rx, ry) ## 루돌프와 산타 간의 거리 계산
    ## 가장 가까운 산타 찾았음

    rudolfColFlag, rux, ruy, nearSan, locru = moveRudolf(santainf) ## 루돌프 이동

    ## 확인
    for i in range(n):
        print(*mapary[i])
        
    if rudolfColFlag: ## 루돌프가 움직여서 충돌한 경우
        rusanCollapse(rux, ruy, nearSan, locru, "Rudolf")

    collapseFlag, colx, coly, colsan, locsan = moveSanta()
    
    print('[-------------')
    for i in range(n):
        print(*mapary[i])

    print(collapseFlag, colx, coly, colsan, locsan)

    if collapseFlag: ## 산타가 움직여서 충돌한 경우
        rusanCollapse(colx, coly, colsan, locsan,  "Santa")