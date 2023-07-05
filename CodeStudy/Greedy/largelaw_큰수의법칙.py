## 큰 수의 법칙

n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

print(n,m,k)
print(arr)

arr.sort(reverse=True) ## 리스트 sort
rslt = 0

## 가장 큰 수를 k번 더하고, 두번째 큰 수를 1번 더하기

fir = arr[0]
sec = arr[1]

print(fir, sec)

while True:
    for num in range(k):
        if m == 0: ## m의 횟수를 줄여나감
            break
        rslt += fir
        m -= 1

    if m == 0:
        break

    rslt += sec
    m -= 1

print(rslt)

## 만약 시간 초과가 발생한다면?? --> 사실 근데 이 문제 이해 가긴 하지만.. 일단 패스