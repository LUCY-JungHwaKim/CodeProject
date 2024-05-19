n = int(input())

ary = list(map(int, input().split()))


def dfs(depth):
    global result

    if len(sol) <= n:
        result.append(sum(sol)) ## 부분수열합 더해서 리스트에 넣어주기

    for i in range(depth+1, n):
        sol.append(ary[i])
        dfs(i)
        sol.pop()


sol = []
result = []



for i in range(n):
    sol.append(ary[i])
    dfs(i)
    sol.pop()

result.sort()
fid = result[0]

if fid != 1: ## 1이 최소값이 아니면, 아래 반복문 할 필요가 없음
    print(1)
else:
    for i in range(1, len(result)):
        if result[i] - fid > 1: ## 이전값이랑 차이가 1 이상 나면
            ## 최소값으로 지정된ㄱ ㅏㅄ +1 해주기
            print(fid+1)
            break
        else: ## 그게 아니라 차이가 1이 나거나,부분수열 합이 같으면 그냥 그대로
            fid = result[i]

    if fid == result[len(result)-1]:
        print(fid + 1)