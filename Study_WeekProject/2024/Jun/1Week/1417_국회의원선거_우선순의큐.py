import heapq

n = int(input())
dasom = int(input())
hq = []

for i in range(n-1):
    num = int(input())
    heapq.heappush(hq, (-num, num)) # 정렬은 첫번째 값을 기준으로, 실제로는 두번째 값을..
    # 다솜의 값이 힙큐의 맨 첫번째 있는 값보다 커야함
    ## 그리고 최소 힙큐라서 작은게 제일 왼쪽에 배치 되는거임


if len(hq) == 0: ## 비어있다면
    print(0)
else:
    cnt = 0
    while True:
        hnum = heapq.heappop(hq)[1] ## heapop은 가장 작은 원소를 pop

        if hnum >= dasom:
            dasom += 1 ## 다솜에게 표가 하나씩 더 주어져야함
            cnt += 1
            heapq.heappush(hq, (-hnum + 1, hnum - 1))

        else:
            break

    print(cnt)
## 어렵군 heapq!!!!!!!!1

## 출처 : https://velog.io/@toezilla/BOJ-1417-%EA%B5%AD%ED%9A%8C%EC%9D%98%EC%9B%90-%EC%84%A0%EA%B1%B0-Python