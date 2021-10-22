from collections import deque

N = int(input())

student_dict = {}

map_ary = [[0 for col in range(N)] for row in range(N)]
dx = [-1, 1, 0, 0] #상, 하, 좌, 우
dy = [0, 0, -1, 1] #상, 하, 좌, 우

for x in range(N**2):   #좋아하는사람 입력받을때마다 계산할 수 있도록 하기 --> 시간 줄여줌
    num_ary = list(map(int, input().split()))
    student_dict[num_ary[0]] = num_ary[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1

    for i in range(N):
        for j in range(N):
            max_neighbor = 0
            if map_ary[i][j] == 0:

                like_cnt = 0
                empty_cnt = 0

                for m in range(4):
                    if (0 <= (i+dx[m]) <= N-1) and (0 <= (j+dy[m]) <= N-1):
                        if map_ary[i+dx[m]][j+dy[m]] in num_ary:
                            like_cnt += 1
                        if map_ary[i+dx[m]][j+dy[m]] == 0:
                            empty_cnt += 1
                
                if max_like < like_cnt or (max_like == like_cnt  and max_empty < empty_cnt):    #좋아하는 학생수가 많거나 또는 비어있는 칸이 가장 많을때
                    #print(max_x, max_y)
                    max_x = i   
                    max_y = j
                    max_like = like_cnt
                    max_empty = empty_cnt
    map_ary[max_x][max_y] = num_ary[0]
cnt_ary = [[0 for col in range(N)] for row in range(N)]
total_score = 0                        
for i in range(N):
    for j in range(N):
        cnt = 0
        for m in range(4):
            if (0 <= (i+dx[m]) <= N-1) and (0 <= (j+dy[m]) <= N-1):
                if map_ary[i+dx[m]][j+dy[m]] in student_dict[map_ary[i][j]]:
                    cnt_ary[i][j] += 1

        if cnt_ary[i][j] == 0:
            total_score += 0
        elif cnt_ary[i][j] == 1:
            total_score += 1
        elif cnt_ary[i][j] == 2:
            total_score += 10
        elif cnt_ary[i][j] == 3:
            total_score += 100
        else:
            total_score += 1000

print(total_score)