# lst = [[1,1,1,1], [2,2,2,2]]
# print(sum(lst[0]))
n_lst = [list(map(int, input().split())) for _ in range(5)] ##철수
loc = [[(0,0) for _ in range(5)] for _ in range(5)]
call_lst = [list(map(int, input().split())) for _ in range(5)] ##사회자
chk = [[0 for _ in range(5)] for _ in range(5)]
lf_cros = [(0,0), (1,1), (2,2), (3,3), (4,4)]
rg_cros = [(0,4), (1,3), (2,2), (3,1), (4,0)]
flag = 0
final_cnt = 0
for i in range(5):
    for j in range(5):
        x = n_lst[i][j] // 5
        y = n_lst[i][j] % 5

        if  y == 0:
            x -= 1
            y = 4
        else:
            y -= 1
        loc[x][y] = (i,j)

for i in range(5):
    for j in range(5):
        x = call_lst[i][j] // 5
        y = call_lst[i][j] % 5

        if  y == 0:
            x -= 1
            y = 4
        else:
            y -= 1

        cx, cy = loc[x][y]
        chk[cx][cy] = 1

        if sum(chk[cx]) == 5:
            flag += 1
        if sum(chk[cy]) == 5:
            flag += 1
        if (cx, cy) in lf_cros:
            num_c = 0
            for m in range(len(lf_cros)):
                num_c += chk[lf_cros[m][0]][lf_cros[m][1]]
            if num_c == 5:
                flag += 1
        if (cx, cy) in lf_cros:
            num_c = 0
            for m in range(len(rg_cros)):
                num_c += chk[rg_cros[m][0]][rg_cros[m][1]]
            if num_c == 5:
                flag += 1
        final_cnt += 1
        if flag == 3:
            print(final_cnt)
            break



