n = int(input())

ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))


def eggdfs(idx):
    global rslt

    ## 만약 끝까지 왔다면? 현재까지 깨진 계란 수 저장하고 탈출

    if idx == n:
        total = 0
        for i in range(n):
            if ary[i][0] <= 0:  ## 내구도가 0 이하면 깨진 거임
                total += 1  ### 깨진 계란 수 저장

        rslt = max(rslt, total)  ## 깰수 있는 계란의 최대 개수
        return

    if ary[idx][0] <= 0:  ## 현재 들고 있는 계란이 깨졌다면?
        eggdfs(idx + 1)  ## 다음꺼로 넘겨줌 계란을
        return

    check = True  # 현재 계란이 다 꺼져있는지 확인하기 위한 것 (자기 빼고)
    for i in range(n):
        if i == idx:  ## 자기 빼고
            continue
        if ary[i][0] > 0:
            check = False
            break
        else:
            check = True

    if check:  ## 다 깨져있는 경우  #자기빼고 전부다니깐 N-1
        rslt = max(rslt, n - 1)

    for i in range(n):
        if i == idx or ary[i][0] <= 0:
            continue
        ary[idx][0] -= ary[i][1]
        ary[i][0] -= ary[idx][1]

        eggdfs(idx + 1)

        ary[idx][0] += ary[i][1]
        ary[i][0] += ary[idx][1]


rslt = 0
eggdfs(0)

print(rslt)