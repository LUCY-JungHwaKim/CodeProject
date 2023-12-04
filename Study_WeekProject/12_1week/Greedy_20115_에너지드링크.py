n = int(input())
from collections import deque
ary = list(map(int, input().split()))

ary.sort(reverse=True) ## 내름차순으로 정렬
drnk = 0
ary = deque(ary)

while ary: ## 큐가 빌 때가지 반복문 돌기
    ## 큰 수들을 앞에서 미리 더해놔야함
    ## 왜냐면 큰 수를 나중에 나눌 수록 더 크게 나눠지기 때문에 많은 양의 에너지를 얻을 수 없음
    fir_ener = ary.popleft()
    sec_ener = ary.popleft()

    cur_fir = fir_ener + (sec_ener/2)
    cur_sec = sec_ener + (fir_ener/2)

    drnk = max(cur_fir, cur_sec)

    ary.appendleft(drnk)

    if len(ary) == 1:
        break

print('%0.5f' %ary[0])
