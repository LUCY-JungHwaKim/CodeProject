str_input =str(input())
str_input = list(str_input.upper())

str_cnt = [0 for i in range(26)] #A to Z


for i in range(len(str_input)):
    cnt = 0
    for j in range(65,91):
        if ord(str_input[i]) == j:
            str_cnt[j-65] += 1

result_ary = []

for i in range(len(str_cnt)):
    if str_cnt[i] == max(str_cnt):
        result_ary.append(chr(i + 65))
   

if len(result_ary) == 1:
    print(result_ary[0])
else:
    print("?")

    
