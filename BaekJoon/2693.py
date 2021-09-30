idx_num = 3
result_ary = []
for i in range(int(input())):
    input_ary = list(map(int, input().split()))
    input_ary = list(reversed(sorted(input_ary)))
    result_ary.append(input_ary[2])

for i in range(len(result_ary)):
    print(result_ary[i])