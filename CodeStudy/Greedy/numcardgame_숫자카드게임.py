##### 이게 내가 작성한 코드
n,m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

max_num = -999

for i in range(n):
    arr[i].sort(reverse=True)

    if arr[i][-1] > max_num:
        max_num = arr[i][-1]

print(arr)

print(max_num)


### 아래 코드가 답안지에 있던 코드
### 내 코드가 sort를 하다보니 정말 긴 배열에서는 시간 초과가 발생할 수 있으므로 아래 코드로 작성하는 것이 더 효과가 있어보임

n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_val = min(data) ## 행마다의 최소값 구하기

    result = max(min_val, result) ## 해당 최소값이 result보다 크다면 result가 결과값이 됨


print(result)