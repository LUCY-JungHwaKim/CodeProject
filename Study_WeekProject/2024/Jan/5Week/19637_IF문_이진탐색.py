n, m = map(int, input().split())

statary = []

for _ in range(n):
    nm, stsnum = map(str, input().split())
    statary.append((nm, int(stsnum)))

numary = []
for _ in range(m):
    numary.append(int(input()))

statary.sort(key=lambda x: x[1])  ## 숫자조건으로 정렬

for num in numary:  ## 숫자 배열을 돌면서 조건 수만큼 while 반복문 진행
    ## 아마 입력된 숫자들이 정렬 된ㅌ채로 입력이 되는듯
    left = 0
    right = len(statary)

    rslt = 0
    # print(statary)
    while left <= right:
        mid = (left + right) // 2
        # print(left, mid, right)
        if statary[mid][1] >= num:  ## 이렇게 해야 나중에 배열이 길어졌을 때, 하나하나 비교해야하는 수고로움을 덜 수 있어서인듯
            # print(statary[mid][1], num)
            rslt = mid
            right = mid - 1
        else:
            left = mid + 1

    print(statary[rslt][0])


