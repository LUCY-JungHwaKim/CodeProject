total_cnt = int(input())




if total_cnt > 0 and total_cnt <= 20:
    ary = [0 for i in range(total_cnt+1)]
    ary[1] = 1
    for i in range(2, total_cnt+1):
        ary[i] = ary[i-1] + ary[i-2]

    print(ary[-1])
else:
    print(0)