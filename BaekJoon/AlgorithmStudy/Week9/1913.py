N = int(input())

num = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
#아래 오른 위 왼

board = [[0]*N for i in range(N)]
answer_x, answer_y = 0,0

x,y,dirs,cnt = 0,0,0, N*N

while True:
    board[y][x] = cnt   # x,y가 아니라 y,x인 이유는 board에서의 인덱스가 반대로이기 때문
    if board[y][x] == num:
        answer_x, answer_y = y+1, x+1
    
    if y == N//2 and x == N//2:
        break
        #정 중앙인 경우
        # 3->(1,1) 5->(2,2) 7->(3,3)

    ny, nx = y + dy[dirs], x+dx[dirs]
    if ny >= N or ny < 0 or nx >= N or nx < 0 or board[ny][nx] != 0:    #if문에도 순서 중요함. 만약 저 board를 앞으로 할 경우
        #인덱스 범위오류로 인해 프로그래밍 오류 날 수 있음
        dirs = (dirs+1)%4 # 다음 진행방향으로
        ny, nx = y + dy[dirs], x+dx[dirs] # 다시 이동

    cnt -= 1
    y,x = ny, nx #바뀐 위치로 좌표 변경

for i in board:
    print(*i)

print(str(answer_x) + " " + str(answer_y))