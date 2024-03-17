import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
## n : 샘터 개수, k : 집 개수

ary = list(map(int, sys.stdin.readline().split()))
q = deque()

visited = set() ## 방문 여부 확인 위한 것

for i in ary:
    q.append((i,1))
    visited.add(i)


minrslt = 0 ## 최솟값
buildh = 0 ## 지어진 집 수

while q:
    x, b = q.popleft()

    for d in [-1, 1]:
        nx = x + d ## 다음 방향

        if nx in visited: ## 방문 여부 체크
            continue ## 방문했었으면 밑에것들 안한다는 뜻


        visited.add(nx) ## 다음 방향 방문

        minrslt += b
        buildh += 1

        q.append((nx, b+1)) ## 1더해준걸로 불행도 넣어주기, 이렇게 하면은 샘터 간의 거리 계산 안해줘도됨

        if buildh == k:
            print(minrslt)
            exit()


