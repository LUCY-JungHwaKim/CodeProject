n = int(input())
m = int(input())

ary = []

for i in range(n):
    ary.append(int(input()))
rslt = []
cnt = 0

def dfs(idx, sol):
    global cnt

    if len(sol) == m:
        strtmp = ""
        for value in sol:
            strtmp += str(value)
        if strtmp not in rslt:
            rslt.append(strtmp)
            cnt += 1
        #print(rslt)
        return


    for i in range(n):
        if chk[i] == 0: ## 선택된 카드는 다시 뽑지 않도록..
            sol.append(ary[i])
            chk[i] = 1
            dfs(i, sol)
            sol.pop()
            chk[i] = 0

chk = [0 for _ in range(n)]

sol = []
for i in range(n):
    sol.append(ary[i])
    chk[i] = 1
    dfs(i, sol)
    sol.pop()
    chk[i] = 0

print(cnt)