import sys

T = int(sys.stdin.readline())

zero_cnt = [1,0,1]
one_cnt = [0,1,1]
# fibo(3) 의 0 호출 횟수 = 2에 대한 0 호출 횟수 + 1에 대한 0 호출횟수
# fibo(3) 의 1 호출 횟수 = 2에 대한 1 호출 횟수 + 1에 대한 1 호출횟수
# 앞의 직전에거만 계속 더하니깐 시간이 오래걸리지도 않음
# 메모리가 터지지도 않음
def fibo(x):
    length = len(zero_cnt)

    if length <= x:
        for i in range(length, x+1):
            zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
            one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
    
    print(zero_cnt[x], one_cnt[x])
    
    
for i in range(T):
    N = int(sys.stdin.readline())
    
    fibo(N)
    





