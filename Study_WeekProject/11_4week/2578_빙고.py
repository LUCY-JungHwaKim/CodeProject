n_lst = [list(map(int, input().split())) for _ in range(5)]  ##철수
loc = [[(0, 0) for _ in range(5)] for _ in range(5)]
call_lst = [list(map(int, input().split())) for _ in range(5)]  ##사회자
chk = [[0 for _ in range(5)] for _ in range(5)]
lf_cros = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)] ## 왼쪽 대각선 위치
rg_cros = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)] ## 오른쪽 대각선 위치

chk_bingo = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0]]
## 가로 빙고 확인, 세로 빙고 확인, 왼/오 대각선 확인

flag = 0  ## 빙고 횟수 카운팅
final_cnt = 0  ## 이동 횟수 카운팅
tot_flag = 0
check_flag = False

for i in range(5): ## 좌표 조절
    for j in range(5):
        x = n_lst[i][j] // 5
        y = n_lst[i][j] % 5

        if y == 0:
            x -= 1
            y = 4
        else:
            y -= 1
        loc[x][y] = (i, j)

# print(loc)

for i in range(5):
    for j in range(5):

        x = call_lst[i][j] // 5
        y = call_lst[i][j] % 5
        # print(x,y, call_lst[i][j])

        if y == 0:
            x -= 1
            y = 4
        else:
            y -= 1

        cx, cy = loc[x][y]
        chk[cx][cy] = 1
        # print('-------------------------')
        # print(x,y,cx,cy)

        # print("------------")
        # print(sum(chk[cx]), sum(chk[cy]))

        if sum(chk[cx]) == 5:  ## 가로 
            # print(cx)
            chk_bingo[0][cx] = 1
            # print(chk_bingo[0], cx)
            # flag += 1

        tmp_sum = 0
        for m in range(5): ## 세로를 확인하기 위해 호출된 숫자가 위치한 열 값 전부 확인하기
            tmp_sum += chk[m][cy]

        if tmp_sum == 5:  ## 세로
            chk_bingo[1][cy] = 1
            # flag += 1

        if (cx, cy) in lf_cros:  ## 왼쪽 대각선
            num_c = 0
            for m in range(len(lf_cros)):
                num_c += chk[lf_cros[m][0]][lf_cros[m][1]]
            if num_c == 5:
                # flag += 1
                chk_bingo[2][0] = 1

        if (cx, cy) in rg_cros:  ## 오른쪽대각선
            num_c = 0
            for m in range(len(rg_cros)):
                num_c += chk[rg_cros[m][0]][rg_cros[m][1]]
            if num_c == 5:
                chk_bingo[2][1] = 1
                # flag += 1

        final_cnt += 1
        # print(chk)
        # print(chk_bingo, final_cnt, (cx,cy))
        lst_sum = sum(sum(chk_bingo, []))
        if lst_sum >= 3:  ## chk_bingo로 확인
            print(final_cnt)
            check_flag = True
            break

    if check_flag == True: ## 이중반복문 탈출을 위한 것
        break    