from collections import deque

def calDistance(loc):

    while loc:
        cx, cy = loc.popleft()

        for i in range(len(dx)) : ## 8방향 탐색
            nx = cx + dx[i]
            ny = cy + dy[i]


            if 0<=nx<n and 0<=ny<m and ary[nx][ny] == 0: ## 방문한 곳만 감
                ## 상어 기준 빈칸이니깐
                loc.append((nx, ny))
                ary[nx][ny] = ary[cx][cy] + 1


if __name__ == "__main__":
    n,m = map(int, input().split())

    ary = []
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    loc = deque()  ## 상어자리 저장할 곳

    for i in range(n):
        inpt = list(map(int, input().split()))
        ary.append(inpt)

        for j in range(m):
            if inpt[j] == 1:
                loc.append((i,j))



    calDistance(loc)
    dist = 0

    for i in range(n):
        for j in range(m):
            dist = max(dist, ary[i][j])

    print(dist - 1) ## 상어부터 시작했으니깐 1 빼줘야함

# 내가 너무 어렵게 생각한듯..처음에 dfs+bfs 했는데 문제르 ㄹ잘못 이해함
# https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-17086%EB%B2%88-%EC%95%84%EA%B8%B0%EC%83%81%EC%96%B4-2-python-bfs