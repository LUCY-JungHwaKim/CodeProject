N = int(input())    #의외로 간단한 문제였음..

first_div = 2
while N != 1:
    if int(N%first_div) == 0:
        N = int(N/first_div)
        print(first_div)
    else:
        first_div += 1