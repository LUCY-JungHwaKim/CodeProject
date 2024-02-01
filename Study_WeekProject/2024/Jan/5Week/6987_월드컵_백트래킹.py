from itertools import combinations as cb

game = list(cb(range(6), 2))  ## 게임 조합


def dfs(start):
    global ans

    if start == 15:  ## 마지막 조합
        ans = 1  ## 가능여부 체크
        for vale in res:
            if vale.count(0) != 3:  # 0이 아닌게 하나라도 있다면?
                ans = 0
                break
        return  ## 종료

    r1, r2 = game[start]  ## 조합 하나씩 꺼내기

    ## 승은 패와 비교, 무는 무와 비교
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[r1][x] > 0 and res[r2][y] > 0:  ## 둘다 값이 있다면?
            res[r1][x] -= 1
            res[r2][y] -= 1
            dfs(start + 1)
            res[r1][x] += 1  ## 위의 if문조건에 해당 안되면 이전 조합 계산했던거 다시 원상 복구
            res[r2][y] += 1

            # DFS(깊이 우선 탐색)를 사용하여 모든 가능한 조합을 탐색합니다.
            # 어떤 조합을 탐색하는 과정에서, 만약 그 조합이 더 이상 진행할 수 없거나 문제의 조건과 맞지 않는 경우(예: 모든 경우의 수를 탐색했지만 조건에 부합하지 않는 경우), 이전 상태로 되돌아갑니다.
            # 되돌아가기 위해, 탐색 과정에서 변경했던 상태(예: res 배열의 값)를 원래대로 복원합니다.
            # 이후 다른 가능한 조합을 탐색합니다.


rslt = []
for i in range(4):  ## 4개만 입력 받는대
    ary = list(map(int, input().split()))  ## 입력
    res = [ary[i:i + 3] for i in range(0, 16, 3)]  # [ary[i*3 : (i*3) + 3] for i in range(6)] 이렇게 하면 틀리네..
    ans = 0
    dfs(0)
    rslt.append(ans)

print(" ".join(map(str, rslt)))