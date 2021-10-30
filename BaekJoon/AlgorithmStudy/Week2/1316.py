N = int(input())

word_ary = []
no_group_word_check = 0
for i in range(N):
    str_input = list(str(input()))

    for j in range(len(str_input)):
        if str_input[j] not in word_ary:
            word_ary.append(str_input[j])
        else:
            if abs(j-str_input.index(str_input[j])) >= 2:
                check_word = 0
                for m in range(str_input.index(str_input[j]), j):
                    if str_input[m] == str_input[j]:
                        check_word += 1
                if check_word != abs(j-str_input.index(str_input[j])):
                    no_group_word_check += 1
                    break

print(N-no_group_word_check)