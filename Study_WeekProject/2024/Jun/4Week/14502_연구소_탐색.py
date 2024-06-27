from collections import deque


def bfs(q, visited): ## 영역 탐색
    cnt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt


def searchAry(lst, visited):
    q = deque()

    cntary = []

    for i in range(n):
        for j in range(m):
            if ary[i][j] == 0 and visited[i][j] == False:
                q.append((i, j))
                visited[i][j] = True
                cnt = bfs(q, visited)
                cntary.append(cnt)

    # print(cntary)

    if len(cntary) == 0:
        return 0
    else:
        return sum(cntary)  ## 영역의 합임 !


def virus(visited):
    virusq = deque(virus_ary)
    # print(virus_ary)
    while virusq:
        cx, cy = virusq.popleft()  # 바이러스 위치를 빼내기

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] == 0 and visited[nx][ny] == False:
                virusq.append((nx, ny))
                visited[nx][ny] = True


def dfs(idx):
    global totalcnt

    if len(sol) == 3:
        # print(sol)
        visited = [[False for _ in range(m)] for _ in range(n)]
        ## 2 를 기준으로 퍼뜨린 다음 0을 찾아야하네..
        virus(visited) ## 먼저 바이러스 퍼뜨리고
        fincnt = searchAry(sol, visited) ## 0부터 탐색해서 영역 크기 찾기
        totalcnt.append(fincnt) ## 모든 영역의 크기를 다 더하는거임
        # print("===========================================")
        # for i in range(n):
        #     print(*ary[i])
        return

    for i in range(idx + 1, zero_len):
        ary[zero_ary[i][0]][zero_ary[i][1]] = 1
        sol.append(zero_ary[i])
        dfs(i)
        sol.pop()
        ary[zero_ary[i][0]][zero_ary[i][1]] = 0


if __name__ == "__main__":

    totalcnt = []
    n, m = map(int, input().split())

    ary = []
    zero_ary = []
    virus_ary = []  ## 바이러스 위치 저장
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        inpt_ary = list(map(int, input().split()))

        for j in range(len(inpt_ary)):
            if inpt_ary[j] == 0:
                zero_ary.append((i, j))

            if inpt_ary[j] == 2:
                virus_ary.append((i, j))
        ary.append(inpt_ary)

    # for i in range(n):
    #     print(*ary[i])

    # print(zero_ary)
    zero_len = len(zero_ary)
    sol = []

    # zero_ary = [(0, 1), (1, 0), (3, 5)]

    for i in range(zero_len):  ## zero_len으로 바꿔야함
        # 처음에 0이 있던 좌표들 중 벽을 세워야함 3개의 벽을 !
        sol.append(zero_ary[i])
        ary[zero_ary[i][0]][zero_ary[i][1]] = 1 ## sol에 넣으면 벽을 세운다는 뜻 1 해줌
        dfs(i)
        sol.pop()
        ary[zero_ary[i][0]][zero_ary[i][1]] = 0 ## 다른 조합으로 가야하니깐 원래 벽 세운곳 0으로 변경

    print(max(totalcnt))

    # print("===========================================")
    # for i in range(n):
    #     print(*ary[i])