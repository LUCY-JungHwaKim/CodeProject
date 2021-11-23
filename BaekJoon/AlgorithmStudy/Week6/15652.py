import sys
from itertools import *

N,M = map(int,sys.stdin.readline().split())

# n_ary =list(range(1,N+1))
# new_ary = {}

# if M > 1 :
#     res = list(product(n_ary, repeat=M))
#     for value in res:
#         value = tuple(sorted(value, key = lambda x: x)) #첫번째 요소 기준으로 오름차순 정렬하고
#         if value not in new_ary:    #새로운 배열에 존재하지않으면 출력하고, 존재하면 넘어가는거 (중복 제거)
#             print(' '.join(map(str,value)))
#             new_ary[value]=1
# else:
#     for i in range(N):
#         print(i+1)
#근데 이렇게 해도되긴하는데 이건 메모리초과 뜸
#순열,조합사용
#https://heytech.tistory.com/78

lst = []
#백트래킹 문제입니다.

def dfs(cnt, idx):

    if cnt-1 == M:
        
        print(" ".join(map(str, lst)))
        return
    
    for i in range(idx, N+1):   # 15651 문제면은 범위 설정을 1,N+1 해야함
        #print(lst)
        lst.append(i)
        dfs(cnt+1, i)
        lst.pop()   #리스트니깐 pop

dfs(1,1)