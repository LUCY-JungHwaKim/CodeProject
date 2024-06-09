n,m = map(int, input().split())

ary = list(map(int, input().split()))

ary.sort()

## 누적합 배열을 만들어 놓기
sumary = [0 for _ in range(n)]

sumary[0] += ary[0] ## 초기 값

for i in range(1, n):
    sumary[i] += sumary[i-1] + ary[i]


rslt = []

for i in range(m):
    a,b = map(int, input().split())

    if a == b: ## 같다면 그냥 현재 값만 출력하면됨
        rslt.append(ary[a-1])
        continue

    if a == 1:
        rslt.append(sumary[b-1])
        continue

    diff = sumary[b-1] - sumary[a-1] + ary[a-1]
    rslt.append(diff)

for i in range(len(rslt)):
    print(rslt[i])

