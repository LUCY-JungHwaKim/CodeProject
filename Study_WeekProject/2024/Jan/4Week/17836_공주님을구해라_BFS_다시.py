from collections import deque
from pydoc import resolve

n, m, t = map(int, input().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))


def findTrway(ary, xs, ys):
    rsltary = []
    q = deque()
    # ary[xs][ys] = 1
    q.append((xs, ys))

    sordx, sordy = 0, 0

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[xs][ys] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    check = False  ### 검 찾았는지
    while q:
        cx, cy = q.popleft()

        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # print(nx,ny)
            if nx < 0 or nx >= n or ny < 0 or ny >= m or ary[nx][ny] == 1 or visited[nx][ny] == True:
                continue  ## 범위를 벗어나거나, 벽을 만나는 경우에 패슨

            if ary[nx][ny] == 2:  ## 검 발견
                sordx, sordy = nx, ny
                check = True

            ary[nx][ny] = ary[cx][cy] + 1
            q.append((nx, ny))
            visited[nx][ny] = True

    if ary[n - 1][m - 1] != 0:  ## 공주를 찾은 경우
        rsltary.append(ary[n - 1][m - 1])

    if check:
        rsltx, rslty = sordx, sordy
        # print(rsltx, rslty)
        ## 검을 찾았는 경우
        if n - 1 - sordx != 0:  ## 밑으로 쭊 내리기
            for i in range(n - 1 - sordx):
                cdx = sordx + (i + 1)
                cdy = sordy
                # print(ary[cdx][cdy], ary[sordx][sordy] + (i+1), ary[sordx][sordy])
                if ary[cdx][cdy] <= 1:
                    ary[cdx][cdy] = ary[sordx][sordy] + (i + 1)
                else:
                    ary[cdx][cdy] = min(ary[cdx][cdy], ary[sordx][sordy] + (i + 1))
            rsltx, rslty = cdx, cdy
        # print(rsltx, rslty)

        if m - 1 - sordy != 0:  ## 오른쪽으로 쭉 밀기
            for i in range(m - 1 - sordy):
                cdx = rsltx
                cdy = rslty + (i + 1)
                if ary[cdx][cdy] <= 1:
                    ary[cdx][cdy] = ary[rsltx][rslty] + (i + 1)
                else:
                    ary[cdx][cdy] = min(ary[cdx][cdy], ary[rsltx][rslty] + (i + 1))

        rsltary.append(ary[n - 1][m - 1])
    # print(ary)
    return rsltary


rslt = findTrway(ary, 0, 0)  ## 먼저 그냥 일반적으로 찾기
for i in range(n):
    for j in range(m):
        print(ary[i][j], end = " ")
    print("")

if rslt and min(rslt) <= t:
    print(min(rslt))
else:
    print("Fail")

# if minary <= t:
#     print(minary)
# else:
#     print("Fail")


