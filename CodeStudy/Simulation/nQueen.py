# # ##### 이게 내가 작성한 코드
loc = list(str(input()))

y = int(ord(loc[0]))-97 ##a,b,c로 나타내는 것들을 아스키 코드로 변환 (ord함수) 
x = int(loc[1])-1

print(x,y)

n = 8 ## n queen의 크기
cnt = 0

dy = [2,2,1,-1, -2, -2, -1, 1] ## 총 움직일 수 있는 경우의 수가 8가지임 (그걸 다 확인)
dx = [1,-1, -2, -2, 1, -1, 2, 2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= n or nx < 0 or ny >= n or ny < 0: ## n의 범위를 벗어난다면 반복문 탈출
        continue ## 요 continue를 쓰면 위 if 조건 문 만족 시, 아래 코드를 실행하지 않고 다음 반복 실행

    cnt += 1

print(cnt)

