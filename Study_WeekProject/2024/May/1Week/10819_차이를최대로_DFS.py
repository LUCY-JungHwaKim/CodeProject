n = int(input())

ary = list(map(int, input().split()))
visited = [False for _ in range(n)]

def dfs(depth):
    global max_ans
    if len(sol) == n:
        ans = 0
        for j in range(n-1):
            ans += abs(sol[j] - sol[j+1])

        max_ans = max(max_ans, ans) ## 값은 계속 갱신하고 있는 거임
        return 


    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sol.append(ary[i])
            dfs(depth + 1)
            visited[i] = False
            sol.pop()

max_ans = -9999
sol = []
depth = 0
dfs(0)
print(max_ans)