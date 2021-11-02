prime_list = []

while True:
    prime_cnt = 0
    N= int(input())

    if N==0:
        break
    
    if N ==1:   # 1인 경우에는 2만 소수이므로 소수카운트는 1로 해줌
        prime_cnt = 1
        prime_list.append(prime_cnt)
    else:   # 그 외에 수는 에라토스테네스의체 --> 범위에서 합성수를 지우는 방식 사용
        #일반적인 방식 사용하면 시간 너무 오래걸림
        check_prime = [0] * ((2*N)+1)
        for i in range(2, (2*N)+1): #2부터 2N까지의 소수 체크
            if check_prime[i] == 0:
                for j in range(i+i, (2*N)+1, i):    #배수별로 체크
                    check_prime[j] = 1

        for i in range(N+1, ((2*N)+1)): #N부터 2N까지 소수 체크
            if i <= 1:
                continue
            else:
                if check_prime[i] == 0:
                    prime_cnt += 1
        prime_list.append(prime_cnt)

for i in range(len(prime_list)):
    print(prime_list[i])
    