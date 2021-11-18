import sys
from itertools import permutations

N,M = map(int,sys.stdin.readline().split())

n_ary =list(range(1,N+1))

if M > 1 :
    res = list(permutations(n_ary, M))
    for value in res:
        print(' '.join(map(str,value)))
else:
    for i in range(N):
        print(i+1)

#순열,조합사용
#https://heytech.tistory.com/78