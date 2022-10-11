N = int(input())

loc_ary = []
person_ary = []
total_sum = 0
for i in range(N):
    x,y = map(int, input().split())
    total_sum += y
    loc_ary.append([x,y])
    

total_person = total_sum // 2   # 사람의 수를 다 더해서 반을 나눈 수를
#넘겼을때의 마을넘버에 우체국을 설치한다는데
#수학적인 이유를 모르겠음..
if total_sum % 2 == 1:
    total_person += 1

loc_ary = sorted(loc_ary, key = lambda x : x[0])
# 1,5 3,2 2,4
# 1,5 2,4 3,2 --> 6

person_cnt = 0
answer = 0
for x,y in loc_ary:
    person_cnt += y
    if person_cnt >= total_person:
        answer = x
        break

print(answer)

# loc_ary = sorted(loc_ary, key = lambda x : x[1], reverse = True)
# person_ary = sorted(loc_ary, key = lambda x : x[0])

# loc_index = 0
# dp = [[0 for i in range(N)] for i in range(N)]


# for i in range(N-1):
#     for j in range(i+1, N):
#         start_home = loc_ary[i][0]
#         next_home = loc_ary[j][0]

#         dp[start_home-1][next_home-1] = abs(start_home-next_home)
#         dp[next_home-1][start_home-1] = dp[start_home-1][next_home-1]


# max_num = -9999
# max_idx = 0
# for i in range(N):
#     home_idx = loc_ary[i][0]-1
#     sum_num = 0
#     for j in range(N):
#         sum_num += dp[home_idx][j]*person_ary[j][1]
#     if sum_num > max_num:
#         max_num = sum_num
#         max_idx = i+1

# print(max_idx)

    
    

