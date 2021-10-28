
str_input = list(str(input()))
result_num = 0


for i in range(len(str_input)):
    dial_num = 0
    if 89 <= ord(str_input[i]) <= 90 or ord(str_input[i]) == 83 or ord(str_input[i]) == 86:  #S,Y,Z만을 제외하고 
        dial_num = (int((ord(str_input[i])-65)/3)+2)
    
    else:
        dial_num = (int((ord(str_input[i])-65)/3))+2+1
    result_num += dial_num
print(result_num)