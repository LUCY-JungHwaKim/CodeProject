from collections import deque

r, c, n = map(int, input().split())

ary = []
bomblst = deque()

for i in range(r):
    ary.append(list(map(str, input())))

## 초기 폭탄 위치 저장
for i in range(r):
    for j in range(c):
        if ary[i][j] == 'O':
            bomblst.append((i, j))


def finbomb(ary, bomblst, n):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # print(newmaps)
    recur_n = int(n // 2)
    for _ in range(recur_n):
        newmaps = [['O' for _ in range(c)] for _ in range(r)]
        while bomblst:

            x, y = bomblst.popleft()  ## 폭탄 위치 꺼내기
            newmaps[x][y] = '.'  ## 폭탄인 곳은 .으로 표시

            for m in range(len(dx)):  ## 네 방향 폭탄 터뜨리기

                cx = x + dx[m]
                cy = y + dy[m]

                if cx < 0 or cx >= r or cy < 0 or cy >= c or newmaps[cx][
                    cy] == '.':  ## 이미 터져있다면 그냥 continue, 그리고 지도 크기에 벗어나면 continue
                    continue

                newmaps[cx][cy] = '.'  ## 폭탄 터뜨리기

        for a in range(r):
            for b in range(c):
                if newmaps[a][b] == 'O':
                    bomblst.append((a, b))

    return newmaps


if n == 1:
    for i in range(r):
        for j in range(c):
            print(ary[i][j], end="")
        print("")
elif n % 2 == 0:
    for i in range(r):
        strm = 'O' * c
        print(strm)
else:
    finmaps = finbomb(ary, bomblst, n)
    for i in range(r):
        for j in range(c):
            print(finmaps[i][j], end="")
        print("")