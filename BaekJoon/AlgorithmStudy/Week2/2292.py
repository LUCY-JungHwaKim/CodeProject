N = int(input())

cnt = 0
flag = 0
while True:
    cnt += flag
    num = (6*cnt) + 1

    if N <= num:
        print(flag+1)
        break
    flag += 1
    