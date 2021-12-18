import sys
import heapq    #우선순위 큐 : 가장 우선순위가 높은 데이터
#default 가 min heap --> 가장 작은 거 먼저 push해줌
# 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, 
#(우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제해야함

N = int(sys.stdin.readline())

room_list = []

for i in range(N):
    x,y = map(int, sys.stdin.readline().split())

    room_list.append([x,y])

room_list = sorted(room_list, key = lambda x : x[0])

#시작시간을 기준으로 정렬해야 하는 이유
#종료시간을 기준으로 정렬한다면 다음 수업시간이 현재 수업시간보다 
#더 일찍 시작할수 있음
#만약 종료 시간을 기준으로 정렬한다면 불필요한 강의실이 늘어날 수 있음
#반례 : 4  -> 1,2 1,4 2,6 4,5
#room_list.sort()
#print(room_list)
room_dict = []

heapq.heappush(room_dict, room_list[0][1])

for i in range(1, N):
    if room_list[i][0] < room_dict[0]:  #현재 강의 시작 시간이 이전강의 끝나는 시간보다 작은 경우에는
        heapq.heappush(room_dict, room_list[i][1])  #룸 추가
    else:   #만약 같거나 크면
        heapq.heappop(room_dict)    #제일 작은 강의 종료시간을 가진 룸을 빼주고
        heapq.heappush(room_dict, room_list[i][1])  #다시 현재 강의의 종료 시간을 다시 큐에 넣어줌
    
print(len(room_dict))

    
        
        