n = int(input())
ary = list(map(int, input().split()))
k = int(input())
stu_lst = []
for i in range(k):
    in1, in2 = map(int, input().split())
    stu_lst.append((in1, in2))

for i in range(k):
    gen, swc = stu_lst[i][0], stu_lst[i][1]

    if gen == 1:  ## 남자일때
        for x in range(n):
            if (x + 1) % swc == 0:  ## 배수인것만 바꿈
                ary[x] = ary[x] ^ 1
    else:  ## 여자일때
        ## 일단 처음과 끝이랑 비교해서 가장 가까운 수 구해서
        ## 비교 횟수 구하기

        strt = swc - 1
        ends = n - swc
        difs = 0

        difs = strt if strt <= ends else ends
        # print(difs)
        ary[strt] = ary[strt] ^ 1  ##XOR 연산

        for i in range(difs):
            befx = (swc - 1) - (i + 1)
            aftx = (swc - 1) + (i + 1)
            # print(befx, aftx)
            if (befx >= 0 and aftx < n):  ## 스위치 범위 내
                if ary[befx] == ary[aftx]:  # 서로 값이 같다면
                    ary[befx] = ary[befx] ^ 1
                    ary[aftx] = ary[aftx] ^ 1
                else:
                    break
            else:
                break

for idx, value in enumerate(ary):
    print(value, end=" ")

    if (idx + 1) % 20 == 0:
        print()
