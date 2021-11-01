M,N = map(int, input().split())

check_prime = [0] * (N+1)

for i in range(2, N+1):
    if check_prime[i] == 0:
        for j in range(i+i, N+1, i):
            check_prime[j] = 1

for i in range(M, N+1):
    if i <= 1:
        continue
    else:
        if check_prime[i] == 0:
            print(i)

#에라토스테네스의체 --> 범위에서 합성수를 지우는 방식
#2의 배수지우고, 3의 배수 지우고, 반복...
