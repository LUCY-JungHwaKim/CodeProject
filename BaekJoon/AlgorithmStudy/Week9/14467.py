N = int(input())

cow_dict = {1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2}  #소의 번호가 1~10번부터니깐 딕셔너리 초기화
change_cnt = 0

for i in range(N):
    cow_num, loc = map(int, input().split())

    if cow_dict[cow_num] == 2:  #현대 소의 위치로 업데이트
        cow_dict[cow_num] = loc
    else:   #만약 초기화값이 아닌 다른 위치라면
        if cow_dict[cow_num] != loc:    #근데 그 값이 같은 값이 아니면 -> 소가 이동하는 것임
            cow_dict[cow_num] = loc #이동하는 위치로 변경하고
            change_cnt += 1 #이동 횟수 더해줌

print(change_cnt)