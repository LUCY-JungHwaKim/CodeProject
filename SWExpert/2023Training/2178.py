
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
chck = 1

r, c = 0,0

from collections import deque

q = deque()

q.append((r,c)) ## 처음 임시 방향 설정 동쪽으로..


dx = [0,0, 1,-1]# 남북동서
dy = [1,-1,0, 0]

#print(arr[3][4])
log = 0
while q:
    r,c = q.popleft()

    for i in range(4):
        curx, cury = r+dy[i], c+dx[i]
        #print(curx, cury)
        #print(curx, cury, i, arr[curx][cury])
        if (0 <= curx < n) and (0 <= cury < m) and (arr[curx][cury] == 1):
                arr[curx][cury] = arr[r][c] + 1
                q.append((curx, cury))
                #chck += 1
    # log += 1
    # if log == 5:
    #     break

## 단순히 마지막 값을 가져오므로
print(arr[n-1][m-1])
