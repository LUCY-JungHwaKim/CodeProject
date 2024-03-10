import sys
from itertools import combinations

N = int(sys.stdin.readline())

ary = []

for _ in range(N):
    ary.append(list(map(int, sys.stdin.readline().split())))

locary = [] ## 씨앗이 심어질 수 있는 곳, 양 모서리 제외
for i in range(1, N-1):
    for j in range(1, N-1):
        locary.append((i,j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
priceary = []

for comb in combinations(locary, 3):
    pricesum = 0
    flowercheck = [[0 for _ in range(N)] for _ in range(N)]  ## 꽃끼리 안겹치게 하기 위한 것

    chk = 0 ## 꽃 세개 체크
    for idx in range(len(comb)): ## 각 조합안에 들어 있는 세 값

        x,y = comb[idx][0], comb[idx][1]

        flowercheck[x][y] = 1
        pricesum += ary[x][y]
        cnt = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and flowercheck[nx][ny] == 0:
                flowercheck[nx][ny] = 1 ## 꽃이 펼진거야.
                pricesum += ary[nx][ny]
                cnt += 1

        if cnt == 5:## 꽃잎이 다섯개 피면 꽃 하나 체크
            chk += 1


    if chk == 3:## 꽃이 세개 일때
        priceary.append(pricesum)



print(min(priceary))

