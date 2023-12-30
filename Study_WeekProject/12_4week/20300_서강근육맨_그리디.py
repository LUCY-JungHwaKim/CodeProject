n = int(input())

ary = list(map(int, input().split()))

ary = sorted(ary)
rslt = -9999999999
if len(ary) % 2 == 0 : ## 짝수일때
    for i in range(n//2):
        tmp = ary[i] + ary[n-i-1]
        rslt = max(tmp, rslt)
else:## 홀수 일때도 마찬가지
    # 근데 홀수일때는 맨 뒤에 (가장 큰 수) 수를 먼저 rslt에 저장
    rslt = ary[-1]
    for i in range(n//2):
        tmp = ary[i] + ary[n-i-2]
        rslt = max(tmp, rslt)
print(rslt)


## 가장 작은값과 큰 값을 더하는 이유가
## 그렇게 해야 최소의 근손실 값이 되기 때문에
## 근손실 정도가 rslt가 넘지 않도록 하고 싶은 거임
#
# [input]
# 5
# 1 2 3 4 100
#
# [ouput]
# 100