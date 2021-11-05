T = int(input())
result_ary = []
for i in range(T):
    room_cnt = 1
    H,W,N = map(int, input().split())
    #층 수 , 각 층의 방 수, 몇번재 손님
    room_num = int(N/H)
    floor_num = int(N%H)

    if floor_num == 0:
        floor_num = str(H)
    else:
        room_num += 1
    if room_num < 10:
        room_num = "0" + str(room_num)
    
    total_room = str(floor_num) + str(room_num)
    result_ary.append(int(total_room))
    
for i in range(len(result_ary)):
    print(result_ary[i])

