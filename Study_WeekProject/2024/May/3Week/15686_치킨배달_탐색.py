n,m = map(int, input().split())

ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))

chk_h = [] ## 치킨집
nor_h = [] ## 일반집
for i in range(n):
    for j in range(n):
        if ary[i][j] == 2:
            chk_h.append((i,j))
        elif ary[i][j] == 1:
            nor_h.append((i,j))
        else:
            continue


def dfs(depth):
    global finary

    #print(sol)


    if len(sol) > m:
        return


    findist = 0
    for i in range(len(nor_h)):
        mindist = 1e+9
        for j in range(len(sol)):
            dist = abs(nor_h[i][0] - sol[j][0]) + abs(nor_h[i][1] - sol[j][1])
            mindist = min(mindist, dist) ## 최소값 구하기

        findist += mindist
    finary.append(findist)
    #print(finary)



    for dx in range(depth+1, len(chk_h)):
        if len(sol) >= m: ## 근데 여기서 >= 해줘야 하는 이유가 잘 와닿지 않음
            ## > 이것만 하면 근데 안됨 왜일까..
            return
        sol.append(chk_h[dx])
        dfs(dx)
        sol.pop()


sol = []
finary = []
for i in range(len(chk_h)):
    sol.append(chk_h[i])
    dfs(i)
    sol.pop()

print(min(finary))

#
# diffary = []
# for i in range(len(nor_h)):
#     mindist = 1e+9
#     for j in range(len(chk_h)):
#         dist = abs(nor_h[i][0] - chk_h[j][0]) + abs(nor_h[i][1] - chk_h[j][1])
#         mindist = min(mindist, dist) ## 최소값 구하기
#
#     diffary.append((nor_h[i][0], nor_h[i][1], mindist))
#
# print(diffary)