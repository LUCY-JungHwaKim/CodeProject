n = int(input())

ary = []

for _ in range(n ** 2):
    ary.append(list(map(int, input().split())))

classary = [[0 for _ in range(n)] for _ in range(n)]  ## 교실 배열

## n이 홀수면 정 중앙에 첫번째 학생 배치, 짝수일때는 어차피 다른 칸들 모두 인접한 칸이 다 비어있을텐데
## 그중에 행과열이 제일 작은거 --> (1,1) 에 위치..


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

if n == 3:# 3일때만 정중앙이네..
    classary[n // 2][n // 2] = ary[0][0]
else: # 짝수 및 다른 수들일때
    classary[1][1] = ary[0][0]  ## 첫번째 학생



# print(classary)
## 첫번째 학생 넣었으니깐 이제 그 다음 학생 넣어야함
## 교실 배열에서, 빈 곳이 있는지 찾기

finscore = 0
for stu in range(1, n ** 2):
    boxlocs = []
    for i in range(n):
        for j in range(n):
            # print(i,j)

            if classary[i][j] == 0:  ## 빈곳이 있다

                ## 4방향 탐색
                idjcnt = 0  ##  인접카운트 수 세아리는거
                boxcnt = 0  ## 그냥 박스 카운트 수
                idjflag = False  ## 인접 플래그
                for m in range(4):
                    ni = i + dx[m]
                    nj = j + dy[m]

                    if 0 <= ni < n and 0 <= nj < n:
                        # print(ni, nj, i, j, ary[stu][1:])
                        if classary[ni][nj] in ary[stu][1:]:
                            idjcnt += 1
                            idjflag = True
                        elif classary[ni][nj] == 0:
                            boxcnt += 1
                        else:
                            continue
                # 첫칸부터 네방향 탐색 - if 탐색 요소 in 좋아하는 사람 - (x,y,인접X칸 수, 인접여부, 인접한 칸 중에 좋아하는 사람이 몇칸인지)
                # 그럼 이 값들을 정렬 기준 : 인접여부(내림차순), 인접O좋아하는칸수(내림차순), 인접O좋아하지않는칸수(내림차순), x(오름차순), y(오름차순)
                boxlocs.append((i, j, boxcnt, idjcnt, idjflag))

    boxlocs = sorted(boxlocs, key=lambda x: (-x[4], -x[3], -x[2], x[0], x[1]))
    finalx, finaly = boxlocs[0][0], boxlocs[0][1]
    classary[finalx][finaly] = ary[stu][0]

# print(finallocs)
# print(classary)

## 점수 구하기
finalscores = 0

ary = sorted(ary, key=lambda x: (x[0]))  ## 어차피 배치는 다 끝났으니깐 정렬 하면 쉽게 좋아하는 학생 가져올 수 있음
# print(ary)
for i in range(n):
    for j in range(n):
        scores = 0
        stuidx = classary[i][j] - 1  ## 위에서 정렬했으니깐 현재 배치된 학생 -1 인덱스를 갖고오면됨
        for m in range(4):
            ni = i + dx[m]
            nj = j + dy[m]

            if 0 <= ni < n and 0 <= nj < n:
                if classary[ni][nj] in ary[stuidx][1:]:  ## 좋아하는 학생 수 카운트
                    scores += 1

        if scores != 0:  ## 0은 0이고, 이외의 점수는 10의 점수-1승만큼 더해짐
            finalscores += (10 ** (scores - 1))
print(finalscores)