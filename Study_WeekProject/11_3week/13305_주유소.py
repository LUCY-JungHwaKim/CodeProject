# n = int(input())
# cities = list(map(int, input().split()))
# prices = list(map(int, input().split()))
#
# ans = 0
# min_price = prices[0]
#
# print(cities)
# print(prices)
# for i in range(n-1):
#     if prices[i] < min_price:
#         min_price = prices[i]
#
#     ans += min_price * cities[i]
#
# print(ans)

n = int(input())
cnt_ct = list(map(int, input().split())) ## 도로간으 ㅣ거ㄹ;
dist = list(map(int, input().split()))

## 일단 맨 처음 도시에서의 주유소 값을 초기 값으로 저장,
## 만약에 다음 도시에서 이전주유소의 돈보다 적으면 해당 값으로 변경
## 그렇지 않으면 이전값으로 계쏙 밀고 가기
## 왜냐면, 제일 적은값으로 도착하는게 제일 이득이기 때문
min_dist = dist[0]
total_cost = 0

for i in range(n-1): ## 도착지점을 제외하고니깐 n-2까지만 확인하면 됨
    #print(i)
    if dist[i] < min_dist:
        min_dist = dist[i]

    total_cost += min_dist * cnt_ct[i]

print(total_cost)

#https://jokerldg.github.io/algorithm/2021/03/16/gas-station.html