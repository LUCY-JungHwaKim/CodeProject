N = int(input())

rope_list = []

for i in range(N):
    rope_list.append(int(input()))

rope_list = sorted(rope_list, reverse=True) #먼저 내림차순으로 정렬

max_num = -9999

for i in range(1,N+1):  
    if i == 1:  #로프 한개만을 사용할 때, 맨 첫번째 숫자만 가져오면 그 값이 최대중량이됨
        max_num = rope_list[i-1]
    else:   # 로프가 여러개 이상일때
        weight_num = rope_list[i-1] * i #만약 로프가 두개 30, 10 짜리면은 이 두개를 사용햇을때의 최대 중량은 10,10이 되므로 20이됨
        #이렇게 맨 마지막 요소를 기준으로 해서 로프 수만큼 곱해주면 그게 최대중량이됨
        if max_num < weight_num:
            max_num = weight_num

print(max_num)
        