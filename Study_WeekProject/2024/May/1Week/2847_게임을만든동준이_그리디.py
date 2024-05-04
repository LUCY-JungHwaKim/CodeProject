n = int(input())
ary = []
for _ in range(n):
    ary.append(int(input()))

ans = 0
max_num = ary[n-1]
for i in range(n-2, -1, -1):
    while max_num <= ary[i]: ## 상위레벨보다 점수가 낮아질때까지 반복
        ary[i] -= 1
        ans += 1

    max_num = ary[i] ## 최대값 갱신


print(ans)