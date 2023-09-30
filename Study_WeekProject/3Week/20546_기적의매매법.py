import sys
input = sys.stdin.readline

cash = int(input())

# 주가 입력
jusik = list(map(int, input().split()))


## 성민이 투자 전략
## 전량 매수 또는 전량 매도
sm_cash = cash
sm_jusik = 0
jh_cash = cash
jh_jusik = 0
max_flag = [0 for _ in range(14)]
min_flag = [0 for _ in range(14)]


## 상민이 방법
for i in range(1, 14):
    ## 3일 연속 가격이 전일 대비 상승하는 주식인 경우 매도함
    if (jusik[i] > jusik[i-1]): ## 산 주식이 있는 경우에만..
        max_flag[i] = 1
        if (i >= 3) & (sum(max_flag[i-2:i+1]) == 3) & (sm_jusik != 0):
            sm_cash += (jusik[i]*sm_jusik)
            sm_jusik = 0

    if (jusik[i] < jusik[i-1]): ## 3일 연속 하락하는 경우
        min_flag[i] = 1
        if (i >= 3) & (sum(min_flag[i-2:i+1]) == 3):
            buy = sm_cash // jusik[i]
            if buy > 0:
                sm_cash = sm_cash - (jusik[i]*buy)
                sm_jusik += buy ## 몇 주 갖고 있다는 것

## 준현이 방법
for i in range(14):
    if jh_cash >= jusik[i]:
        if_buy = jh_cash // jusik[i]
        jh_jusik += (if_buy)
        jh_cash = jh_cash - (jusik[i]*if_buy)

jh_result = jh_cash + (jusik[i]*jh_jusik)
sm_result = sm_cash + (jusik[-1]*sm_jusik)

if jh_result > sm_result:
    print("BNP")
elif jh_result < sm_result:
    print("TIMING")
else:
    print("SAMESAME")