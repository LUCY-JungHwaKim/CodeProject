n = int(input())
ary = list(map(str, input()))
arydict = {'B':0, 'R':0}
arydict[ary[0]] += 1
cur_s = ary[0]
for i in range(1, len(ary)): ## 다른문자 발견할때만 더하기 1해주기
    if ary[i] != cur_s:
        arydict[ary[i]] += 1
        cur_s = ary[i]
#print(arydict)
minum = min(arydict['B'], arydict['R'])
print(minum+1)ㅌ