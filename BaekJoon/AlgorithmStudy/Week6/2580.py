import sys

total_data = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros_loc = [(i,j) for i in range(9) for j in range(9) if total_data[i][j] == 0]

#print(zeros_loc)
total_cnt = 0

def check_num(i,j):
    ##print(i,j)

    available_num = [1,2,3,4,5,6,7,8,9]
    #먼저 행열 검사
    for m in range(9):
        if total_data[i][m] in available_num:
            available_num.remove(total_data[i][m])
        if total_data[m][j] in available_num:
            available_num.remove(total_data[m][j])

    # 3*3 block 검사

    i //= 3 #박스찾기
    j //= 3

    for x in range(i*3, (i+1)*3):
        for y in range(j*3, (j+1)*3):
            if total_data[x][y] in available_num:
                available_num.remove(total_data[x][y])

    return available_num

flag = False
def find_num(idx):
    global flag

    if flag:    #이렇게 해줘야함,, 아니면 그냥 밑에 len검사할때 sys.exit() 해줘야함
        return

    if idx == len(zeros_loc):
        for row in total_data:
            print(*row)
        flag = True
        return
    else:
        i,j = zeros_loc[idx]

        promising_num = check_num(i,j)  #사용가능한 숫자 찾기
        
        for num in promising_num:
            total_data[i][j] = num
            find_num(idx+1)
            total_data[i][j] = 0    #그다음 해가 없으면 다시 0으로 만들어서 다음 사용가능한 숫자 테스트 하기

find_num(0)