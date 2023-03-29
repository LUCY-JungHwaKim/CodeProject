
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
chck = 0

r, c = 0,0

from collections import deque

q = deque()

q.append((r,c,0)) ## 처음 임시 방향 설정 동쪽으로..

visited[r][c] = 1

dx = [0,0, 1,-1]# 남북동서
dy = [1,-1,0, 0]
rev_nav = [1,0,3,2]
print(arr)
#print(arr[3][4])
log = 0
while q:
    r,c,d = q.popleft()
    print(r,c,d)
    nav_chk = 0
    for i in range(4):
        curx, cury = r+dy[i], c+dx[i]
        #print(curx, cury)
        #print(curx, cury, i, arr[curx][cury])
        if (0 <= curx < n) and (0 <= cury < m):
            if (arr[curx][cury] == 1) and (visited[curx][cury] == 0):
                r,c = curx, cury
                print('---')
                print(r,c,i)
                visited[r][c] = 1
                q.append((r,c,i))
                chck += 1
                break
        else:
            nav_chk += 1

    if nav_chk == 4:
        cur_d = rev_nav[d]
        curx, cury = r + dy[cur_d], c+dx[cur_d]
        q.append((curx, cury, d))
        chck -= 1

    # log += 1
    # if log == 5:
    #     break


print(chck)
