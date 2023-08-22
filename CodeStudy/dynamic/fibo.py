 ## 계산 결과 저장하는 리스트

d = [0] * 100

def fibo(x):
    if x ==1  or x == 2:
        return 1

    if d[x] != 0: #계산한 결과가 있다면
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    # 아직 계산하지 않았다면 점화식에 따라 값 넣고 return
    return d[x]

print(fibo(30))