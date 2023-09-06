## 디피
## 근데 사실 순열조합 문제인걸로 보임
## 조합 먼저 !!! ## 근데 조합으로 풀리면 시간초과 하는 듯함
# from itertools import combinations, permutations
## 조합 모듈 쓰면 오래 걸리는 것 같음

T = int(input())

inp_ary = []
for i in range(T):
    n,m = map(int, input().split())
    inp_ary.append((n,m))

d = [0] * 30
d[1] = 1
d[2] = 2
## 처음 값 초기화

for i in range(3, len(d)): ##최대 사이트 수가 작으므로, dp알고리즘 사용해서 이전값에 계속 곱해줌으로써 값 저장
    d[i] = i*d[i-1]

result_ar = []
for i in range(T):
    if (inp_ary[i][0] == inp_ary[i][1]): ## n,m이 같다면 1가지 경우만 있음
        result_ar.append(1)
    elif (inp_ary[i][0] == 1): ## n=1인 경우에는m값 출력
        result_ar.append(inp_ary[i][1])
    else: ## 조합 수식 활용
        targ = inp_ary[i][1]-inp_ary[i][0]

        sons = d[inp_ary[i][1]]
        result = sons/(d[targ]*d[inp_ary[i][0]])

        result_ar.append(result)

for j in range(len(result_ar)):
    print(int(result_ar[j]))

#==========================

import math

T = int(input())
result_ary = []
for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    ##실제 모듈 사용해서 팩토리얼 구현 가능
    ## 조합 수식 사용
    result_ary.append(bridge)

for j in range(len(result_ary)):
    print(result_ary[j])