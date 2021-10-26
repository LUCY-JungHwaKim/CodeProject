
# cnt = 0

# N = int(input())

# first_num = int(N/10)
# second_num = int(N%10)
# cnt = 0
# while 0<= N <=99:
    

#     one_cycle = first_num + second_num
#     new_num = second_num*10 + int(one_cycle%10)
#     first_num = int(new_num/10)
#     second_num = int(new_num%10)
#     cnt += 1

#     if new_num == N:
#         print(cnt)
#         break


# N = int(input())

# num_ary = list(map(int, input().split()))

# print(min(num_ary), max(num_ary))

# num_ary = []

# for i in range(9):
#     N = int(input())
#     num_ary.append(N)
    
# print(max(num_ary))
# print(num_ary.index(max(num_ary))+1)

# a = int(input())
# b = int(input())
# c = int(input())

# mul_num = list(str(a*b*c))
# for i in range(10):
#     print(mul_num.count(str(i)))

# num_ary = []
# for i in range(10):
#     N = int(input())
#     num_ary.append(N%42)

# result_ary = set(num_ary)
# print(len(result_ary))

# N = int(input())
# num_ary = list(map(int, input().split()))
# max_score = max(num_ary)

# total_sum = 0
# for i in range(N):
#     num_ary[i] = (num_ary[i]/max_score)*100
#     total_sum += num_ary[i]

# print(total_sum/N)

# N = int(input())

# num_ary = []
# for i in range(N):
#     str_ary = []
#     input_str = list(input())
#     str_cnt = 0
#     str_sum = 0
#     for j in range(len(input_str)):
#         if input_str[j] == 'O':
#             str_cnt += 1
#         else:
#             str_cnt = 0
#         str_sum += str_cnt
#     num_ary.append(str_sum)

# for i in range(N):
#     print(num_ary[i])

# N = int(input())

# percent_ary = []

# for i in range(N):
#     score_ary = list(map(int, input().split()))
#     avg_num = sum(score_ary[1:])/score_ary[0]
#     cnt = 0
#     for j in range(score_ary[0]):
#         if score_ary[j+1] > avg_num:
#             cnt += 1
#     percent_ary.append((cnt/score_ary[0])*100)

# for i in range(N):
#     print("{:.3f}%".format(percent_ary[i]))


# num_ary = list(map(int, input().split()))

# total_sum = 0
# for i in range(len(num_ary)):
#     total_sum += num_ary[i]



# num_ary = [i+1 for i in range(10000)]
# result_ary = []

# idx = 0

# for i in range(10000):
    
#     num = sum(map(int, str(i+1))) + i + 1

#     #print(sum(map(int, str(i+1))))
#     if  num in num_ary and num <= 10000 :
#         #print(num,i+1)
#         result_ary.append(num)

# result_ary = set(result_ary)

# for i in sorted(set(num_ary)-result_ary):
#     print(i)
