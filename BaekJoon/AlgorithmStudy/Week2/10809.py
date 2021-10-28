
alpha_ary = []

for i in range(97,123):
    alpha_ary.append(chr(i))

input_str = list(str(input()))

alpha_num_ary = [-1 for _ in range(len(alpha_ary))]

for i in range(len(input_str)):
    if input_str[i] in alpha_ary:
        idx_alpha = alpha_ary.index(input_str[i])
        alpha_num_ary[idx_alpha] = input_str.index(input_str[i])

for i in range(len(alpha_num_ary)):
    print(str(alpha_num_ary[i]) + " ", end='')