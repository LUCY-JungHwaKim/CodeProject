N = int(input())

sum_num = 0
start_num = 1
while 1:
    sum_num += start_num

    if sum_num > N:
        print(start_num-1)
        exit()
    
    start_num += 1