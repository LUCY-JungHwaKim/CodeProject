## https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    # nonlocal answer
    answer = -1
    curtired = k
    curdun = []
    visited = [False for _ in range(len(dungeons))]

    # curdun.append(dungeons[i])
    visitCnt = 0

    def dfs(k, visitCnt):
        nonlocal answer

        answer = max(answer, visitCnt)

        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and visited[i] == False:
                visited[i] = True
                dfs(k - dungeons[i][1], visitCnt + 1)
                visited[i] = False
            # print(i)

    dfs(k, 0)

    return answer

