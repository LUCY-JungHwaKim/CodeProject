n = int(input())

ary = [0]
## 점화식이랑 인덱스 맞추려면 ary의 길이는 n+1 해야함

for _ in range(n):
    ary.append(int(input()))

dp = [0 for _ in range(n + 1)]
# print(len(dp), len(ary))
## 어려워 미치겠다 DP
## 초기화
dp[1] = ary[1]
if n > 1:
    dp[2] = ary[1] + ary[2]

###  dp  점화식
# n =3 기준으로 (dp[0]을 사용해야함)

# X O O X = dp[2]
# O X O O = dp[0] + ary[2] + ary[3]
# X O X O = dp[1] + ary[3]

##근데 이게 반복됨
# n = 4일 때도 마찬가지
# dp[0]은 생각하지말고
# X O O X = dp[3] (0인건 계산된다 가정)
# O X O O = dp[1] + ary[3] + ary[4] (여기서 dp[1]은 dp[0]까지 더해진것)
# X O X O = dp[2] + ary[4] (여기서 dp2는 dp[0] + ary[2]까지 계산된 것)
## 같은 패턴이 반복됨


for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + ary[i - 1] + ary[i], dp[i - 2] + ary[i])

print(dp[n])