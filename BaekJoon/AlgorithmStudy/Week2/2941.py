
word_ary = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str_input = str(input())

word_cnt = 0
sub_word = []


word_idx = 0
not_found_flag = 0
while True:
    if word_ary[word_idx] in str_input:
        word_cnt += 1
        sub_word.append(word_ary[word_idx])
        str_input = str_input.replace(word_ary[word_idx], "/")  #해당 단어가 있으면 / 로 치환
        word_idx = 0
    
    else:
        word_idx += 1
    
    
    if word_idx == len(word_ary):   #끝까지 찾았고 모든 단어를 다시 첨부터 끝까지 검색했을때 어떠한 단어도 포함하고 있지않으면 while문 종료
        no_found_flag = 0
        for i in range(len(word_ary)):
            if word_ary[i] not in str_input:
                no_found_flag += 1
        if no_found_flag == len(word_ary):
            break

    
print(len(str_input))
