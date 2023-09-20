import math
n = int(input())

d = [0 for _ in range (n+1)]
d[0] = 0
d[1] = 1


for i in range(2, n+1):
    minval = 999 ## 최소값 비교를 해줘야하므로 초기 최소값은 제일 크게 잡아줌
    j = 1

    while j**2 <= i: # 자기 자신 이전에 제곱값이 있다면
        minval = min(minval, d[i-(j**2)]) ## 현재 값에서 제곱값을 뺀 값의 dp값확인(최소 개수 확인)

        j += 1

    d[i] = minval + 1
print(d[n])

https://star7sss.tistory.com/200