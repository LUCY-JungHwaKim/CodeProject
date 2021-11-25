
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
#메모이제이션 -> 저장하기
#저장을 하면 다음 연산때 있던 값 불러오면 되고 다시 계산 안해도 됨
# 사실 쉬운 문제인데 dp개념이 조금덜 잡힌듯
def calculate(a,b,c):
    if a <= 0 or b <=0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return calculate(20,20,20)
    if dp[a][b][c]: #값이 존재하면 해당 값 return
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = calculate(a,b,c-1) + calculate(a,b-1, c-1) - calculate(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = calculate(a-1, b, c) + calculate(a-1, b-1, c) + calculate(a-1, b, c-1) - calculate(a-1, b-1, c-1)
    return dp[a][b][c]


while 1:
    a,b,c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    value = calculate(a,b,c)
    print(f'w({a}, {b}, {c}) = {value}')


