n = int(input())

nsize = 2 * (2 * (n - 1)) + 1  ##전체 사이즈 맵
maps = [[' ' for _ in range(nsize)] for _ in range(nsize)]
# print(maps)

ncnt = int(n // 2) + 1  ## 반복문 도는 횟수

### 중심점 찍기
cx, cy = 2 * (n - 1), 2 * (n - 1)
# print(cx, cy)
maps[cx][cy] = '*'
dfscnt = int(cx // 2)


# import numpy as np

def drawstart(maps, ncnt, nsize, n, cx, cy, dfscnt):  ## idx는 현재 카운팅 횟수

    # mapnary = np.array(maps)

    for idx in range(dfscnt):
        nx = cx - (2 * (idx + 1))
        ny = cy + (2 * (idx + 1))
        # print(nx, ny)
        # mapnary[[nx, ny], nx:ny+1] = '*'
        # mapnary[nx:ny+1, [nx, ny]] = '*'
        for i in range(nx, ny + 1):  ## 넘파이 지원안한대 백준은
            maps[nx][i] = '*'
            maps[ny][i] = '*'
            maps[i][nx] = '*'
            maps[i][ny] = '*'

        # print(mapnary)
    # maps = mapnary.tolist()

    return maps


rsltmap = drawstart(maps, ncnt, nsize, n, cx, cy, dfscnt)

for i in range(nsize):
    # print(*rsltmap[i], end='')
    # print("") ### 이렇게 출력하면 출력 결과가 이상하게 보임
    print(''.join(rsltmap[i]))  # 얘ㅒ로 해야함 띄어쓰기 없는걸로

# lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# lst[1] = [1] * len(lst[1])