T = int(input())

prime_list = {}

check_prime = [0] * (10001)
check_prime[0] = 1
check_prime[1] = 1

for i in range(2, 10001):
    if check_prime[i] == 0:
        for j in range(i+i, 10001, i):
            check_prime[j] = 1




for _ in range(T):
    minus_min = 99999
    N = int(input())

    for i in range(2,N):
        cal_result = N-i
        if (check_prime[i] == 0) and (check_prime[cal_result] == 0):
            if abs(cal_result-i) < minus_min:
                minus_min = cal_result-i
                prime_list[N] = i


for idx, (key, value) in enumerate(prime_list.items()):
    print(str(value) + " " + str(int(key-value)))
