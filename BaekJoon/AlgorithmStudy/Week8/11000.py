import sys
N = int(sys.stdin.readline())

room_list = []

for i in range(N):
    x,y = map(int, sys.stdin.readline().split())

    room_list.append((x,y))

room_list = sorted(room_list, key = lambda x : x[1])

room_dict = set()
room_num = 0
room_dict.add(room_list[0][1])
    
for i in range(1, N):
    if room_list[i][0] in room_dict:
        room_dict.add(room_list[i][1])
        