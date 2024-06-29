from collections import deque



if __name__ == "__main__":

    n,k = map(int, input().split())
    maxk = 100000

    q = deque()
    q.append(n)
    distary = [0 for _ in range(maxk+1)]

    while q:
        cur = q.popleft()

        if cur == k:
            break

        for nx in (cur-1, cur+1, cur*2): ## 방문하지 않았다면 탐색
            if 0<=nx<=maxk and distary[nx] == 0:
                distary[nx] = distary[cur] + 1
                q.append(nx)

    print(distary[k])