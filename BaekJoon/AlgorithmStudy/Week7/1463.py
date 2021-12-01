import sys

N = int(sys.stdin.readline())

#10을 구할 때는 9의 결과를
#9를 구할 때는 3의 결과를
#그래서 오름차순으로 올라가면서 연산 횟수를 저장하기..

dp = [0 for i in range(N+1)]

for i in range(2, N+1): #N+1을 하는 이유는 인덱스를 N의 개념으로 하기 위해서
    dp[i] = dp[i-1]+1   # 2나 3으로 나누어지지 않는다면 무조건 1을 빼야함

    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

# Ex) N = 9 라면, dp[8]+1, dp[3]+1 중에서 최솟값을 선택해야함
print(dp[N])