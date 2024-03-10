
import sys
from collections import deque
import math

N ,M ,K = map(int, sys.stdin.readline().split())
## N : 격자 크기, M : 파이어볼 개수, K : 이동 명령 횟수

# r,c : 위치(나중에 할때는 -1 해줘야함), m : 질량, s: 속력, d : 방향#

ballinfo = []
ballary = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M): ## 파이어볼 정보 입력
    r ,c ,m ,s ,d = map(int, sys.stdin.readline().split())
    ballinfo.append(( r -1 , c -1)) ## 파이어볼 위치 기록용
    ballary[ r -1][ c -1].append([m ,s ,d, 1]) ## 질량,속력,방향 넣기 , 여기서 1은 지정하는것
    ## 만약 0이라면 이전 파이어볼이 이동돼서 움직인 곳이라는 것
    # ballary[r-1][c-1] += 1 ## 파이어볼 체크
ballinfo = deque(ballinfo)
#print(ballary)
# 0부터 7까지 순서대로
dx = [-1 ,-1, 0, 1, 1, 1, 0, -1 ]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def moveball():
    #print(ballinfo)
    fir_ballength = len(ballinfo)
    for _ in range(fir_ballength):
        cx, cy = ballinfo.popleft()
        # print(ballary[cx][cy], cx, cy)
        ballary[cx][cy].sort(key=lambda x : x[3])

        tmpbalary = len(ballary[cx][cy])
        #print(ballary[cx][cy][-1], cx, cy)
        for _ in range(tmpbalary):
            if ballary[cx][cy][-1][3] == 1: ## 옮겨야 하는 파이어볼만
                curm ,curc ,curd = ballary[cx][cy][-1][0], ballary[cx][cy][-1][1], ballary[cx][cy][-1][2]
                # ballary[cx][cy] -= 1 ## 이 파이어볼이 이동할 거니깐 -1

                tmpc = curc ## 새로운 변수에 해줘야함, 아니면 나눠진 값이 큐에 들어가게됨 ㅠㅠ
                if curc >= N:
                    tmpc = curc % N


                nx = cx + (dx[curd] * tmpc)
                ny = cy + (dy[curd] * tmpc)

                if nx < 0:
                    nx += N
                if nx >= N:
                    nx -= N
                if ny < 0:
                    ny += N
                if ny >= N:
                    ny -= N
                #print("----")

                ballary[cx][cy].pop() ## 맨 뒤에꺼 빼기

                ballary[nx][ny].append([curm ,curc ,curd, 0]) ## 파이어볼 개수 체크
                #print(ballary)
                ## 옮긴거는 0으로 표시
                ## 이전 파이어볼이 원래 있던 파이어볼 자리로 이동해서 겹쳐지는 것 같은데..
                #if (nx,ny) not in ballinfo: ## 똑같은거 두번 안넣얻도 되니깐
                ballinfo.append((nx, ny)) ## 이동하기 전의 파이어볼 질량이랑넣기

        #print(ballary)
        # ballary[cx][cy] = []

def checkball():
    checkary = []
    for i in range(N):
        for j in range(N):
            if len(ballary[i][j]) >= 2:
                checkary.append((i ,j))
    return checkary


def divideball(balloc): ## 파이어볼 나누기 --> 같은 칸 안에서 나누는 거임
    #print(ballinfo)
    for i in range(len(balloc)):
        ax, ay = balloc[i][0], balloc[i][1]
        msum, ssum = 0, 0
        dcnt = [0, 0] ## 짝홀 카운팅
        for x in range(len(ballary[ax][ay])):
            msum += ballary[ax][ay][x][0] ## 질량 더하기
            ssum += ballary[ax][ay][x][1] ## 속력 더하기

            if ballary[ax][ay][x][2] % 2 == 0: ##짝수라면
                dcnt[0] += 1
            else: ## 홀수라면
                dcnt[1] += 1

        msum = math.floor(msum /5)
        ssum = math.floor(ssum /len(ballary[ax][ay]))
        dary = [] ## 네개로 나누어질때의 파이어볼 방향
        if dcnt[0] == len(ballary[ax][ay]) or dcnt[1] == len(ballary[ax][ay]):
            ## 방향들이 모두짝수이거나 홀수라면?
            dary = [0 ,2 ,4 ,6]
        else:
            dary = [1 ,3 ,5 ,7]

        # ===========파이어볼 재분배 해야함 =========
        ballary[ax][ay] = []
        if msum != 0  :## 질량이 0이면 소멸 되므로
            for i in range(4):
                ballary[ax][ay].append([msum, ssum, dary[i], 1])

def changeball(ballinfo):
    for i in range(len(ballinfo)):
        ax, ay = ballinfo[i][0], ballinfo[i][1]
        for x in range(len(ballary[ax][ay])):
            if ballary[ax][ay][x][3] == 0:
                ballary[ax][ay][x][3] = 1

def calm(balloc):
    totalm = 0
    for i in range(len(balloc)):
        ax, ay = balloc[i][0], balloc[i][1]
        for x in range(len(ballary[ax][ay])):
            totalm += ballary[ax][ay][x][0] ## 질량 더하기

    return totalm

for _ in range(K):
    moveball() ## 파이어볼 이동
    #print("after move")
    #print(ballary)
    balloc = checkball() ## 파이어볼이 두개 있는 칸인지 검사
    #print("check ball")
    #print(balloc)
    divideball(balloc) ## 파이어볼 나누기
    #print("devide ball")
    #print(ballary)
    ballinfo = deque(set(ballinfo))
    #print(ballinfo)
    #print(balloc)
    ## 0으로 되어 있는 파이어볼 들을 1로 바꿔주기
    changeball(ballinfo)
    #print("changeball")
    #print(ballary)
    #print("=======================================")

finm = calm(ballinfo) ## 질량합구하기
print(finm)



############################원래 내꺼
# import sys
# from collections import deque
# import math

# N,M,K = map(int, sys.stdin.readline().split())
# ## N : 격자 크기, M : 파이어볼 개수, K : 이동 명령 횟수

# #r,c : 위치(나중에 할때는 -1 해줘야함), m : 질량, s: 속력, d : 방향#

# ballinfo = []
# ballary = [[[] for _ in range(N)] for _ in range(N)]
# moveary = [[[] for _ in range(N)] for _ in range(N)] ## 파이어볼이 이동했을때 저장하는 곳

# for _ in range(M): ## 파이어볼 정보 입력
#     r,c,m,s,d = map(int, sys.stdin.readline().split())
#     ballinfo.append((r-1,c-1)) ## 파이어볼 위치 기록용
#     ballary[r-1][c-1].append((m,s,d)) ## 질량,속력,방향 넣기
#     #ballary[r-1][c-1] += 1 ## 파이어볼 체크
# ballinfo = deque(ballinfo)
# print(ballary)
# #0부터 7까지 순서대로
# dx = [-1,-1, 0, 1, 1, 1, 0, -1 ] 
# dy = [0, 1, 1, 1, 0, -1, -1, -1]

# def moveball():
#     print("hi")
#     print(ballary[1][5], ballinfo)
#     fir_ballength = len(ballinfo)
#     for _ in range(fir_ballength):
#         cx, cy = ballinfo.popleft()
#         print(ballary[cx][cy], cx, cy)
#         for x in range(len(ballary[cx][cy])):
#             curm,curc,curd = ballary[cx][cy][x][0], ballary[cx][cy][x][1], ballary[cx][cy][x][2]
#             #ballary[cx][cy] -= 1 ## 이 파이어볼이 이동할 거니깐 -1

#             if curc >= N:
#                 curc = curc % N


#             nx = cx + (dx[curd]*curc)
#             ny = cy + (dy[curd]*curc)

#             if nx < 0:
#                 nx += N
#             if nx >= N:
#                 nx -= N
#             if ny < 0:
#                 ny += N
#             if ny >= N:
#                 ny -= N

#             ballary[nx][ny].append((curm,curc,curd)) ## 파이어볼 개수 체크
#             ## 이전 파이어볼이 원래 있던 파이어볼 자리로 이동해서 겹쳐지는 것 같은데..
#             if (nx,ny) not in ballinfo: ## 똑같은거 두번 안넣얻도 되니깐
#                 ballinfo.append((nx, ny)) ## 이동하기 전의 파이어볼 질량이랑넣기

#         ballary[cx][cy] = []

# def checkball():
#     checkary = []
#     for i in range(N):
#         for j in range(N):
#             if len(ballary[i][j]) >= 2:
#                 checkary.append((i,j))
#     return checkary


# def divideball(balloc): ## 파이어볼 나누기 --> 같은 칸 안에서 나누는 거임

#     for i in range(len(balloc)):
#         ax, ay = balloc[i][0], balloc[i][1]
#         msum, ssum = 0, 0
#         dcnt = [0, 0] ## 짝홀 카운팅
#         for x in range(len(ballary[ax][ay])):
#             msum += ballary[ax][ay][x][0] ## 질량 더하기
#             ssum += ballary[ax][ay][x][1] ## 속력 더하기

#             if ballary[ax][ay][x][2] % 2 == 0: ##짝수라면
#                 dcnt[0] += 1
#             else: ## 홀수라면
#                 dcnt[1] += 1

#         msum = math.floor(msum/5)
#         ssum = math.floor(ssum/len(ballary[ax][ay]))
#         dary = [] ## 네개로 나누어질때의 파이어볼 방향
#         if dcnt[0] == len(ballary[ax][ay]) or dcnt[1] == len(ballary[ax][ay]):
#             ## 방향들이 모두짝수이거나 홀수라면?
#             dary = [0,2,4,6]
#         else:
#             dary = [1,3,5,7]

#         #===========파이어볼 재분배 해야함 =========
#         ballary[ax][ay] = []
#         if msum != 0:## 질량이 0이면 소멸 되므로
#             for i in range(4):
#                 ballary[ax][ay].append((msum, ssum, dary[i]))

# def calm(balloc):
#     totalm = 0
#     for i in range(len(balloc)):
#         ax, ay = balloc[i][0], balloc[i][1]
#         for x in range(len(ballary[ax][ay])):
#             totalm += ballary[ax][ay][x][0] ## 질량 더하기

#     return totalm

# for _ in range(K):
#     moveball() ## 파이어볼 이동
#     print(ballary)
#     balloc = checkball() ## 파이어볼이 두개 있는 칸인지 검사
#     print(balloc)
#     divideball(balloc) ## 파이어볼 나누기
#     print(ballary)
#     print(ballinfo)
#     print(balloc)
#     print("=======================================")

# finm = calm(ballinfo) ## 질량합구하기
# print(finm)


