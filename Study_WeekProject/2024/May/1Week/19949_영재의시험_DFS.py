ary = list(map(int, input().split()))


def dfs(depth):
    global cnt

    if depth == 10:
        score = 0
        for j in range(10):
            if ary[j] == sol[j]:
                score += 1

        if score >= 5:
            cnt += 1

        return

    for i in range(1, 6):  ## 정답 고르기
        if depth > 1 and sol[depth - 2] == sol[depth - 1] == i:
            continue
        sol.append(i)
        dfs(depth + 1)
        sol.pop()


sol = []
cnt = 0
dfs(0)
print(cnt)

