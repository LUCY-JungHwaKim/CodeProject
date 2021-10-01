a,b = map(int, input().split())

a_divisor_list = list(filter(lambda y : a%y == 0 ,list(range(1,a+1))))
b_divisor_list = list(filter(lambda y : b%y == 0 ,list(range(1,b+1))))

common_list = []
max_num = 1

for i in range(len(a_divisor_list)):
    for j in range(len(b_divisor_list)):
        if a_divisor_list[i] == b_divisor_list[j]:
            common_list.append(a_divisor_list[i])

print(max(common_list))

print(max(common_list) * (a//max(common_list)) * (b//max(common_list)))
