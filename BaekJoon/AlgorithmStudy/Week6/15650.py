import sys
from itertools import permutations

N,M = map(int,sys.stdin.readline().split())

n_ary =list(range(1,N+1))
new_ary = []

if M > 1 :
    res = list(permutations(n_ary, M))
    for value in res:
        value = tuple(sorted(value, key = lambda x: x)) #첫번째 요소 기준으로 오름차순 정렬하고
        if value not in new_ary:    #새로운 배열에 존재하지않으면 출력하고, 존재하면 넘어가는거 (중복 제거)
            print(' '.join(map(str,value)))
            new_ary.append(value)
else:
    for i in range(N):
        print(i+1)

#순열,조합사용
#https://heytech.tistory.com/78