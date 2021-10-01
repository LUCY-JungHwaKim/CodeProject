cnt_num = int(input())

num_ary = list(map(int, input().split()))
cnt = 0

for i in range(cnt_num):
    num_divisor_list = list(filter(lambda x: num_ary[i] % x == 0, list(range(1, num_ary[i]+1))))
    if len(num_divisor_list) == 2:
        cnt += 1
print(cnt)