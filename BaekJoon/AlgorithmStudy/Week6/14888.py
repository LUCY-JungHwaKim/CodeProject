import sys
N = int(input())

N_ary = list(map(int, sys.stdin.readline().split()))
a,b,c,d = map(int, sys.stdin.readline().split())
result_ary = []

result_num = 0
def operate_num(result,idx, a,b,c,d):
    global result_ary
    if a == 0 and b == 0 and c == 0 and d == 0:
        result_ary.append(result)
        return
    
    # if idx == len(N_ary):
    #     return result

    if a > 0:
        operate_num(result+N_ary[idx+1], idx+1, a-1, b,c,d)
    if b > 0:
        operate_num(result-N_ary[idx+1], idx+1, a, b-1, c, d)
    if c > 0:
        operate_num(result*N_ary[idx+1], idx+1, a, b, c-1, d)
    if d > 0:
        operate_num(int(result/N_ary[idx+1]), idx+1, a, b, c, d-1)

    
    return  result_ary



operate_num(N_ary[0], 0, a,b,c,d)
print(max(result_ary))
print(min(result_ary))