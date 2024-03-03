import heapq

n = int(input())

for _ in range(n):
    J, N = map(int, input().split())
    h = [] ## 힙큐 생성

    for _ in range(N):
        r,c = map(int, input().split())

        h.append((-r*c, r, c))

    heapq.heapify(h)
    boxcnt = 0 ## 박스 개수
    boxsum = 0 ## 사탕 개수
    for x in range(len(h)):
        ax = heapq.heappop(h)

        #print(ax, ax[0])

        boxsum += (-ax[0]) ## 힙큐의 우선순위를 내림차순으로 바꿔주기 위해
        boxcnt += 1

        if boxsum >= J: ## 사탕개수보다 넘으면 출력
            break


    print(boxcnt)
