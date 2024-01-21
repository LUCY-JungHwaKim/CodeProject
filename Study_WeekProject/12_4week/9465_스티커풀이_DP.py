n = int(input())
m_lst = []
ary_lst = []
## 아쉽당 ㅠㅠ
## 너무이전값이랑 더한다고생각하지말아야할듯 ㅠㅠ
##dP어려워

for i in range(n):

    m = int(input())
    m_lst.append(m)

    ary = []

    for j in range(2):
        ary.append(list(map(int, input().split())))

    ary_lst.append(ary)

rslt = []

for i in range(n):
    solary = ary_lst[i]
    lns = m_lst[i]

    if lns >= 2:

        solary[0][1] += solary[1][0]  # 초기값
        solary[1][1] += solary[0][0]

        for j in range(2, lns):  ##열의 개수만큼
            ## 직전 대각선까지의 합 구하기 # 대각선 두개까지만
            solary[0][j] = max(solary[0][j] + solary[1][j - 1], solary[0][j] + solary[1][j - 2])
            solary[1][j] = max(solary[1][j] + solary[0][j - 1], solary[1][j] + solary[0][j - 2])
        # print(solary)
        rslt.append(max(solary[0][lns - 1], solary[1][lns - 1]))
    else:
        rslt.append(max(solary[0][0], solary[1][0]))

for x in rslt:
    print(x)