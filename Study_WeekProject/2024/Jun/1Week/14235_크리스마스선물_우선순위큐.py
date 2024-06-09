import heapq

n = int(input())

hq = []
rslt = []

for _ in range(n):
    lst = list(map(int, input().split()))

    if lst[0] == 0: ## 첫번째가 0이라면?
        if hq :
            print(heapq.heappop(hq)[1]) ## 제일 앞에 있는거 출력
        else: ## 그냥 아무것도 없는거니깐
            print(-1)
    else:
        for i in range(1, lst[0]+1):
            heapq.heappush(hq, (-lst[i], lst[i])) # 최소힙을 최대힙으로 바꿔주기 위해서

## 내가 잘못생각한게 0일때 출력해야하는데
## a가 입력될 때도 출력해버렸음..