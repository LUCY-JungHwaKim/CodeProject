import sys
N = int(input())

N_ary = list(map(int, sys.stdin.readline().split()))
a,b,c,d = map(int, sys.stdin.readline().split())
result_ary = []

result_num = 0
def operate_num(result,idx, a,b,c,d):
    if a == 0 and b == 0 and c == 0 and d == 0:
        return result
    
    if idx == len(N_ary):
        return result

    if a > 0:
        operate_num(N_ary[idx]+N_ary[idx+1], idx+1, a-1, b,c,d)
    elif b > 0:
        operate_num(N_ary[idx]-N_ary[idx+1], idx+1, a, b-1, c, d)
    elif c > 0:
        operate_num(N_ary[idx]*N_ary[idx+1], idx+1, a, b, c-1, d)
    elif d > 0:
        operate_num(int(N_ary[idx]/N_ary[idx+1]), idx+1, a, b, c, d-1)

    return result








result = operate_num(N_ary, 0, a,b,c,d)
print(result)