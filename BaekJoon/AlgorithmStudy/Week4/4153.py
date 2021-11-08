result = []

while True:
    num = list(map(int, input().split()))
    max_num = max(num)  #맨 마지막 숫자가 제일 클거라는 보장이 없기 때문

    

    if num[0] == 0 and num[1] == 0 and num[2] == 0:    #종료 구문
        for i in range(len(result)):
            print(result[i])
        break

    num.remove(max_num)
    
    if num[0]**2 + num[1]**2 == max_num**2:
        result.append("right")
    else:
        result.append("wrong")