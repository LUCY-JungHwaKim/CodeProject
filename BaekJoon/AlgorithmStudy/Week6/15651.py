import sys
from itertools import *

N,M = map(int,sys.stdin.readline().split())

n_ary =list(range(1,N+1))

if M > 1 :
    res = list(product(n_ary, repeat=M))    #중복순열

    for value in res:
        print(' '.join(map(str,value)))
else:
    for i in range(N):
        print(i+1)

#순열,조합사용
#https://heytech.tistory.com/78