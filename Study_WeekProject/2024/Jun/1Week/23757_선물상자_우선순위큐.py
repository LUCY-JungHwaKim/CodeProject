import heapq

n,m = map(int, input().split())

gift_ary = list(map(int, input().split()))
child_ary = list(map(int, input().split()))
gift_hq = []

for i in range(len(gift_ary)):
    heapq.heappush(gift_hq, (-gift_ary[i], gift_ary[i]))

## 아이들은 순서대로 번호가 쥐어진다 했음
## 나는 아이들도 heaqp로 처리해버렸는데 그러면 안됨!!!!


checkcnt = 0
for i in range(len(child_ary)):
    childnum = child_ary[i]
    giftnum = heapq.heappop(gift_hq)[1]

    if childnum > giftnum: ## 현재 아이가 가질 수 없는 상자가 있으면 반복문 탈출
        break
    else:
        diff = giftnum - childnum
        ## 선물상자에서 선물 가져가고
        ## 남은 선물 개수는 다시 선물 힙큐에 넣어주기

        if diff > 0:
            heapq.heappush(gift_hq, (-diff, diff))

        checkcnt += 1 ## 선물 가져갈 수 있음

if checkcnt == m: ## 애들 다 선물 가져갈 수 있다면?
    print(1)
else:
    print(0)