N = int(input())

num_list = list(map(int, input().split()))

cnt = 0


for i in range(len(num_list)):
    if num_list[i] == 1:
        continue
    else:
        minor_cnt = 0
        for j in range(2, num_list[i]+1):   #2부터 시작이므로 1은 이미 포함한다고 가정
            if num_list[i]%j == 0:
                minor_cnt += 1
                if minor_cnt > 1:
                    break
        if minor_cnt == 1:
            cnt += 1

print(cnt)