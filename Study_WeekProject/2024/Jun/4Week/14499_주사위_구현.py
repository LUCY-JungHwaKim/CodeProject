import sys


def roll_north(dice):
    dice[0], dice[2], dice[1], dice[3] = dice[2], dice[1], dice[3], dice[0]


def roll_south(dice):
    dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]


def roll_east(dice):
    dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]


def roll_west(dice):
    dice[0], dice[5], dice[1], dice[4] = dice[5], dice[1], dice[4], dice[0]


if __name__ == "__main__":

    n, m, x, y, k = map(int, sys.stdin.readline().split())

    ## 세로, 가로, 좌표 xy, 명령 개수

    mapary = []  ## 지도

    for i in range(n):
        mapary.append(list(map(int, sys.stdin.readline().split())))

    dirary = list(map(int, sys.stdin.readline().split()))  # 방향 배열

    dice = [0, 0, 0, 0, 0, 0]  ## 위, 아래, 앞, 뒤, 왼, 오

    curx, cury = x, y  ## 현재 주사위가 놓여져있는 좌표
    rslt = []
    changeFlag = False
    # print(dirary)

    for i in range(len(dirary)):
        if dirary[i] == 1 and 0 <= cury + 1 < m:  ## 동, 방향이내라면 이동 가능
            roll_east(dice)
            cury += 1
            changeFlag = True
        elif dirary[i] == 2 and 0 <= cury - 1 < m:  ## 서
            roll_west(dice)
            cury -= 1
            changeFlag = True
        elif dirary[i] == 3 and 0 <= curx - 1 < n:  ## 북
            roll_north(dice)
            curx -= 1
            changeFlag = True
        elif dirary[i] == 4 and 0 <= curx + 1 < n:  ## 남
            roll_south(dice)
            curx += 1
            changeFlag = True

        # print(curx, cury)

        if 0 <= curx < n and 0 <= cury < m and changeFlag == True:
            if mapary[curx][cury] == 0:  # 이동한 칸에 쓰여있는 수가 0이면,
                ## 주사위 바닥면 쓰여있는 수가 복사됨
                mapary[curx][cury] = dice[1]
            else:  ## 0이 아니라면
                ## 칸에 쓰여있는 수가 주사위 바닥면으로 복사됨
                dice[1] = mapary[curx][cury]
                ## 칸에 쓰여있는 수는 0이 됨
                mapary[curx][cury] = 0

            # print(dice)
            rslt.append(dice[0])
            changeFlag = False

    for i in range(len(rslt)):
        print(rslt[i])



