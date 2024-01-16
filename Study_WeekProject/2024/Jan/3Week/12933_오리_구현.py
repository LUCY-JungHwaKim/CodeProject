from collections import deque
ary = list(map(str, input()))

visited = [False for _ in range(len(ary))]
cnt = 0 # 마리수

if len(ary) %5 != 0: ## quackquack이라고 안함
    print(-1)
    exit() # 종료

def findduck(strt):
    global cnt
    quack = 'quack'
    j = 0
    first = True ##한마리가 계속 부르는지 확인하는 것
    for i in range(strt, len(ary)):
        if ary[i] == quack[j] and visited[i] == False:
            ## quack 차례대로 맞으면 한마리임
            visited[i] = True
            if ary[i] == 'k': ## 한마리가 다 불렸다면?
                if first:
                    cnt += 1
                    first = False # 얘가 계속 부르는 거니깐 False로 해줌
                j = 0
                continue
            j += 1

for i in range(len(ary)):
    if ary[i] == 'q' and visited[i] == False:
        findduck(i)

if not all(visited) or cnt == 0: ## quack 대로 하지 않았거나, 모두 방문하지 않은 경우
    ## 즉, 오리가 소리를 제대로 안낸 것
    print(-1)
else:
    print(cnt)


# https://tmdrl5779.tistory.com/128
    # 구현 너무 어렵다