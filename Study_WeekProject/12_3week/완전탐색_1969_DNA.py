n, m = map(int, input().split())
ary = []
result = ''
for i in range(n):
    tmpary = list(map(str, input()))
    ary.append(tmpary)
total = 0
for i in range(m):  ## 문자열 길이
    cnt = [0, 0, 0, 0]  ## A,C,G,T
    for j in range(n):
        if ary[j][i] == 'A':
            cnt[0] += 1
        elif ary[j][i] == 'C':
            cnt[1] += 1
        elif ary[j][i] == 'G':
            cnt[2] += 1
        elif ary[j][i] == 'T':
            cnt[3] += 1
    idxcnt = cnt.index(max(cnt))
    if idxcnt == 0:
        result += 'A'
    elif idxcnt == 1:
        result += 'C'
    elif idxcnt == 2:
        result += 'G'
    elif idxcnt == 3:
        result += 'T'
    total += n - max(cnt)

print(result)
print(total)
## https://yuna0125.tistory.com/112