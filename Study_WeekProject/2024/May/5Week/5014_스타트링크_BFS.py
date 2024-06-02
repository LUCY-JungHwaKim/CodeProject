from collections import deque
f,s,g,u,d = map(int, input().split())

q = deque([s])
ary = [0 for _ in range(f+1)]
ary[s] = 1 ## 방문 체크

while q:

    curs = q.popleft()
    if curs == g:
        break
    ## 위로 가는거
    if 0< curs+u <= f and ary[curs+u] == 0: ## 전체 수보다 낮고, 방문하지 않은 층이라면
        q.append(curs+u)
        ary[curs+u]  = ary[curs] + 1

    if 0< curs-d <= f and ary[curs-d] == 0 :### 전체 수보다 낮고, 방문하지 않은 층이라면
        q.append(curs-d)
        ary[curs-d]  = ary[curs] + 1

if ary[g] == 0:
    print("use the stairs")
else:
    print(ary[g] - 1) ## 1 빼줘야하는건 처음에 s에 대해 초기값 할때 1로 해줬기 때문에