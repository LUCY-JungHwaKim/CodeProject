n,m = map(int, input().split())
d = [1 for _ in range(101)]

def factorial(d, x):
    if x == 1:
        return d[x]
    d[x] = x * factorial(d, x-1)
    return d[x]


if n == m :
    print("1")

if n > m:
    n_fac = factorial(d, n) ## 먼저 큰 수에 대해서 팩토리얼을 구했으면, 이보다 작은 수는 이미 배열에 저장 되어 있음

    result = int(n_fac // (d[n-m] * d[m]))  # //와 / 차이가 난다고 함

    print(result)
