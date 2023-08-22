
n,m = map(int, input().split())

ary = list(map(int, input().split()))

## 가장 길이가 긴 떡의 길이 만큼 크기 ? 생성

start = 0
end = max(ary)

## 이진 탐색 수행
result = 0

while start <= end:
    ## 절단기의 높이를 중간점으로 지정

    ## 중간점 지정 후 잘랐을 때 남는 떡의 양이 손님이 원하는 양보다 크다면, 시작점을 중간점+1로 변경
    total = 0
    mid = (start + end ) // 2

    for x in ary:
         # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += (x-mid)

    if total >= m: ## 떡의 양이 충분한 경우 덜 자르기
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)