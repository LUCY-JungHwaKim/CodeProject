n,m = map(int, input().split())


ary = []

for _ in range(n):
    ary.append(list(map(int, input().split())))


def dfs(idx, sol, finary):

    if len(sol) <= 3:
        maxary = []
        for x in range(n):## 사람 수만큼
            max_per = 0 # 사람 별 max 값
            for val in sol:
                max_per = max(max_per, ary[x][val]) ## 사람 별 max 값 갱신
            maxary.append(max_per)
        finary.append(sum(maxary)) ## 경우의 수별 합 구하기
        # print(finary)
    else: ## 이 조건 필수! 안그러면 시간 초과 남
            
        return


    for i in range(idx+1, m):
        sol.append(i)
        dfs(i, sol, finary)
        sol.pop()

finary = []
sol = []
for i in range(m):
    sol.append(i)
    dfs(i, sol, finary)
    sol.pop()

print(max(finary))