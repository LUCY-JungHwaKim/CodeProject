N = int(input())

num_ary = list(str(input()))

sum = 0
for i in range(len(num_ary)):
    sum += int(num_ary[i])

print(sum)