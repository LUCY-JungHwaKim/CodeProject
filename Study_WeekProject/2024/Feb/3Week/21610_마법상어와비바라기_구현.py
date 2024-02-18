from traceback import print_stack

n, m = map(int, input().split())

ary = []  ## 전체 배열

for _ in range(n):  ## n by n 행렬
    ary.append(list(map(int, input().split())))

dirary = []  ## 이동방향 배열

for _ in range(m):
    a, b = map(int, input().split())  ## 방향, 몇 번 이동할 지 입력
    dirary.append((a, b))

# print(ary)
## 2. 이동 방향만큼 이동
## 먼저, 이동방향에 따른 좌표 이동 값 초기화
dirway = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
crossway = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

## 비바라기 시전 --> (N, 1), (N, 2), (N-1, 1), (N-1, 2) 에 비 구름이 생김 
## 초기 비구름 생성
cloudary = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
## 얘는 처음 구름 초기화 값이랑, 추후에 모든 이동을 끝 마치고 나서 구름 위치 ㅈ저장할 리스트

totalsum = 0  ## 바구니에 들어있는 물의 양

for i in range(m):
    ## 비구름을 체크용
    cloudchk = [[0 for _ in range(n)] for _ in range(n)]
    cloudflagq = []  ## 좌표 이동 후, 구름의 위치를 넣는 것

    dir = dirary[i][0] - 1  ##  방향, 입력받을때 1더해서 받으므로 1 빼줘야함
    cnt = dirary[i][1]  ## 얼마나 움직일 건지

    if cnt >= n:  ## cnt가 n보다 큰 경우도 처리해줘야 함
        cnt = cnt % n
    # print(dir, cnt)
    cloudcnt = len(cloudary)  ## 구름 개수
    for _ in range(cloudcnt):

        ## 구름을 이동 시켜서 1로 해줘야 함

        x, y = cloudary.pop()  ## 끝에서 빼내기 하나하나씩

        nx = x + (dirway[dir][0] * cnt)
        ny = y + (dirway[dir][1] * cnt)

        ## 이동하는 좌표가 0보다 작으면 n씩 더해주고, 0보다 크면 n 빼줌
        if nx < 0:
            nx += n
        if ny < 0:
            ny += n
        if nx >= n:
            nx -= n
        if ny >= n:
            ny -= n

        cloudchk[nx][ny] = 1  ## 여기에 이제 비가 내리는 거니깐
        cloudflagq.append((nx, ny))
        # print(cloudchk)
        ## 얘 있어야해!!

        ## 원본 리스트의 비 양 증가시켠주기
        ary[nx][ny] += 1

        # print(ary)
    flaglen = len(cloudflagq)

    for _ in range(flaglen):
        ## 대각선 방향 탐색 (물복사 마법)
        flagx, flagy = cloudflagq.pop()

        watercnt = 0  ## 물 있는지 체크
        for _, (cx, cy) in enumerate(crossway):

            nsx = flagx + cx
            nsy = flagy + cy
            # print(flagx, flagy, cx, cy, nsx, nsy) 
            ## 배열의 범위 안에 있다면, 물이 없다면
            if nsx < 0 or nsx >= n or nsy < 0 or nsy >= n or ary[nsx][nsy] == 0:
                continue

            watercnt += 1
        # print(watercnt)
        ary[flagx][flagy] += watercnt  ## 물 있는 대각선 수 만큼 구름의 물 양 더해주기
        # print(ary)

    ## 구름을 재 지정해줘야 함
    ## 물의 양이 2 이상인게 구름으로 설정되고, 설정이 되면 값이 -2 씩 줄어듦
    # print(ary)
    # print(cloudchk)
    for a in range(n):
        for b in range(n):
            if ary[a][b] >= 2 and cloudchk[a][b] == 0:  ## 이전에 구름이 아닌애들을 구름 리스트에 넣어줘야해
                cloudary.append((a, b))  ## 구름 리스트에 위치를 넣어줌
                ary[a][b] -= 2  ## 2씩 물의 양을 빼줌

    # print(cloudary)
    # print(ary)

totalsum = sum(sum(inner_list) for inner_list in ary)
print(totalsum)