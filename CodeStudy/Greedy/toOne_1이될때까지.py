
## 1을 빼는게 있고, K로 나누는게 있는데
## 일반적으로 나누는게 한 번에 많은 수가 깎임

n, k = map(int, input().split())
cnt = 0

while n > 1:

    if (n // k == 0) & (n < k): ## n을 k로 나눈 몫이 0이고, n이 k보다 작은 경우 예) n=4, k=5인 경우에는 n에서 1을 계속 빼야함
        print(n,k)
        n -= 1
        cnt += 1

    else:   ## 그렇지 않은 경우에는 k로 나눠서 업데이트 여기서 중요한거는 int형으로 몫이 나눠질 수 있게 해야 함
        print(n,k)
        n //= k
        cnt += 1

print(cnt)

