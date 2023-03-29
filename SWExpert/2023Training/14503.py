## ㅂㅏㅇㅎㅑㅇ ㅅㅓㄹㅈㅓㅇ

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

##ㅊㅓㅇㅡㅁ ㅂㅏㅇㅁㅜㄴ ㅊㅔㅋㅡ
visited[r][c] = 1
cnt = 1

from collections import deque


# q = deque()
# q.append((r, c, d))

while True:
    clear_flag = 0
    #r, c, d = q.popleft()


    for _ in range(4):
        #cur_d = chng_d[cur_d]
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
            cnt += 1
            #q.append((nr, nc, d))
            r = nr
            c = nc
            clear_flag = 1
            break

    if clear_flag == 0:
        #print(d)
        #back_curd = back_d[d]
        #print(r,c,back_curd)
        #nr, nc = r - dr[d], c - dc[d]
        if arr[r - dr[d]][c - dc[d]] == 1:
            print(cnt)
            break
        else:
            #q.append((nr,nc,d))
            r,c = r-dr[d], c-dc[d]

