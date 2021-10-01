start_num = int(input())
end_num = int(input())

total_minor_list = []

for i in range(start_num, end_num+1):
    if i > 1:   #소수는 1이 포함안된다는걸 까먹지 마세요.
        flag = 0
        for j in range(2, i):
            if i % j == 0:  #나누어떨어지는게 하나라도 있으면 그 수는 소수가 아니니깐 if문 걸었음 --> 굳이 람다로 1부터 자기자신까지 검사할 필요가 없음
                flag += 1
                break
        if flag == 0:
            total_minor_list.append(i)

if len(total_minor_list) > 0:
    print(sum(total_minor_list))
    print(min(total_minor_list))
else:
    print(-1)
