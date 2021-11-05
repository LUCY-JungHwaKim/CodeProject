

def recursive(k, n):    #재귀는 쉽게 돌아갈수 있음 , 헷갈리지말기
    count = 0
    if k == 0:
        return n
    else:
        for i in range(1,n+1):
            count += recursive(k-1, i)
    return count
    
T = int(input())

for _ in range(T):
    k = int(input())    #층
    n = int(input())    #호
    print(recursive(k,n))


# for _ in range(T):
#     k = int(input())    #층
#     n = int(input())    #호


        
                