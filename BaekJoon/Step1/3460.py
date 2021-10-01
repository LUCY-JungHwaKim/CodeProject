        
for i in range(int(input())):
    case_input = int(input())

    one_cnt = 0
    while case_input > 0:
        if case_input % 2 == 1:
            print(str(one_cnt), end=" ")
        case_input = case_input // 2 #나누기 하고 소수점 버리고 정수부분만 남긴다는 연산자

        one_cnt += 1
    