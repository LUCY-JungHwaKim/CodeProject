from collections import deque

def findRoute(idx):

    q = deque()
    q.append(idx) ## 첫번째 요소 넣기..
    visited[idx] = 1 ## 방문 표시하기
    cnt = 0

    while q:
        cx = q.popleft()

        if len(dict[cx]) != 0:
            for i in range(len(dict[cx])):
                if visited[dict[cx][i]] == 0: ## 값이 있다면?, 그 곳이 방문하지 않은 곳이라면?
                    q.append(dict[cx][i])
                    visited[dict[cx][i]] = 1 ## 방문표시
                    cnt += 1

    return cnt


if __name__ == "__main__":
    n,m = map(int, input().split())

    dict = {i+1 : [] for i in range(n)}
    visited = [0] * (n+1)

    for i in range(m):
        a,b = map(int, input().split())

        dict[a].append(b)
        dict[b].append(a) ## 이걸 해줘야함

    cntary = []
    for i in range(1, len(visited)):
        if visited[i] == 0:
            fincnt = findRoute(i)
            cntary.append(fincnt)

    print(len(cntary))