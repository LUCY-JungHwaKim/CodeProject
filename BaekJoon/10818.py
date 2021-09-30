

num_cnt = int(input())
ary = [0 for i in range(num_cnt)]
input_num = list(map(int, input().split()))
if len(input_num) == num_cnt:
    print(str(min(input_num)) + " " + str(max(input_num)))
