from collections import deque

n, l, r = map(int,input().split())

ary = []

for i in range(n):
    ary.append(list(map(int,input().split())))

totalmap = []


## 벽 경계가 생긴 map 생성 완료 --> totalmap

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):

    q = deque()
    rsltary = []
    q.append((x, y))
    rsltary.append((x, y))

    while q:

        cx, cy = q.popleft()

        for i in range(len(dx)):
            nx = cx + dx[i]
            ny = cy + dy[i]
            ## 전역변수인 visited를 쓸 수 있는 이유 : 수정을 하지 않기 때문에 사용 가능
            # 수정해야 한다면 global 키워드 사용해야 함
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                diffv = abs(ary[cx][cy] - ary[nx][ny])

                if l <= diffv <= r:
                    visited[nx][ny] = 1 ## 사이에 값이존재한다면 방문 표시
                    q.append((nx, ny)) ## 어차피 전체만큼 돋ㄹ아가니깐 사이에 값 존재할때만ㅇ ㅜㅁ직이면됨
                    rsltary.append((nx, ny))


    return rsltary
 ## 내가 너무 어렵게 생각한 것 같다

cnt = 0
while True:
    visited = [[0] * (n+1) for _ in range(n+1)]
    flag = 0 ## 인구이동 체크

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                cntry = bfs(i,j) ## 국경선이 열렸다면
                if len(cntry) > 1:
                    flag = 1
                    numb = sum([ary[x][y] for x,y in cntry]) // len(cntry)
                    for x,y in cntry:
                        ary[x][y] = numb ## 인구수 변경

    if flag == 0:
        break

    cnt += 1

print(cnt)

