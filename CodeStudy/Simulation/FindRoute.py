# # ##### 이게 내가 작성한 코드
n = int(input())

arr = list(map(str, input().split()))

dx = [-1, 1, 0, 0] ## 상, 하, 좌, 우
dy = [0, 0, -1, 1]
str_type = [ 'U', 'D','L', 'R']

str_x = 0
str_y = 0

for strt in arr:

    for i in range(len(str_type)): # 4방향 탐색
        if strt == str_type[i]: # 해당 인덱스를 가지는 방향 값을 더해줌
            str_x += dx[i]
            str_y += dy[i]

        if (str_x> n-1) | (str_x < 0) | (str_y > n-1) | (str_y < 0):
            # 만약 범위를 벗어난다면? 위에서 했던 작업 취소하면 됨
            str_x -= dx[i]
            str_y -= dy[i]


print(str_x + 1, str_y + 1) ## 나는 0,0을 시작지점으로 설정했으므로 마지막에 출력할때 1을 더해줘야함


## 해석코드


# n = int(input())
#
# arr = list(map(str, input().split()))
# x,y = 1,1
#
# dx = [-1, 1, 0, 0] ## 상, 하, 좌, 우
# dy = [0, 0, -1, 1]
# str_type = [ 'U', 'D','L', 'R']
#
#
#
# for strt in arr:
#
#     for i in range(len(str_type)): # 4방향 탐색
#         if strt == str_type[i]: # 해당 인덱스를 가지는 방향 값을 더해줌
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#     if (nx> n) | (nx < 1) | (ny > n) | (ny < 1):
#         continue ## 공간을 벗어나는 경우 무시
#
#     x,y = nx, ny
#
#
# print(x,y) ## 나는 0,0을 시작지점으로 설정했으므로 마지막에 출력할때 1을 더해줘야함