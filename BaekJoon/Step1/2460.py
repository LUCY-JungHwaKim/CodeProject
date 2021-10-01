current_num = 0
max_list = [0 for i in range(10)]
for i in range(10):
    descend_num, ascend_num = map(int, input().split())
    
    current_num = current_num-descend_num+ascend_num
    max_list[i] = current_num
print(max(max_list))