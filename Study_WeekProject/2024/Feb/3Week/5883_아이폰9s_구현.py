n = int(input())
ary = []

for _ in range(n):
    ary.append(int(input()))

flag = False
totalcnt = -999
flag = False

valueunique = list(set(ary))
#print(valueunique)

for x in valueunique:
    firvale = -1
    cnt = 0
    for i in range(len(ary)):
        if x == ary[i]:
            continue
        #print(x, firvale, ary[i], cnt)

        if firvale != ary[i]:
            firvale = ary[i]
            cnt = 0
        else:
            cnt += 1

        totalcnt = max(totalcnt, cnt)

print(totalcnt+1)

