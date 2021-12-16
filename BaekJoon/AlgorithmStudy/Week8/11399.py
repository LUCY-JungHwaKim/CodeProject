#DP+Greedy문제같음

N = int(input())

time_list = list(map(int, input().split()))

time_list = sorted(time_list)   #오름차순으로 정렬하고

dp = [0 for _ in range(N)]
dp[0] = time_list[0]

for i in range(1,N):
    dp[i] = dp[i-1] + time_list[i]  #현재 시간과 앞사람 시간을 더해줌
    time_list[i] = time_list[i-1] + dp[i]   # 위의값을 이전의 time 시간에 계속해서 더해주면
    #최종적으로 최소하게 소요되는 시간을 계산할 수 있음

print(time_list[N-1])
