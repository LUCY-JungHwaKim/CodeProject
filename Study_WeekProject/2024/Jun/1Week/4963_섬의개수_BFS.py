from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    cnt = 1


    while q:
        cx, cy = q.popleft()
        

        
        for i in range(len(dx)):
            
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0<=nx<h and 0<=ny<w and ary[nx][ny] == 1: ## 갈만한 곳이라면
                q.append((nx, ny)) ## 큐에서 넣을때
                ary[nx][ny] = 0 ## 이렇게 방문표시해야함, 
                ## 큐에서 뺀 다음에 하면 여러 칸에서 동시에 같은 칸 방문할 때, 그 칸이 큐에 여러번 들어가게 됨
                cnt += 1


    return cnt
                



if __name__ == "__main__":

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    while True:
        ary = []
        landary = []
        w, h = map(int, input().split())

        if w == 0 or h == 0:
            break

        for _ in range(h):
            ary.append(list(map(int, input().split())))


        for i in range(h):
            for j in range(w):
                if ary[i][j] == 1:
                    ary[i][j] = 0  ## 방문 표시 해줘야 다음 탐색할때 재 탐색 안함
                    landcnt = bfs(i,j)
                    landary.append(landcnt)

        print(len(landary))