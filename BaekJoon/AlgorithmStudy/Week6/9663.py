N = int(input())
total_cnt = 0
board = [0 for _ in range(N)]
visited = [False for _ in range(N)]
#리스트의 인덱스 --> 체스판의 행
#리스트의 값 --> 체스판의 퀸이 놓인 열의 위치


def queen(n):
    if n == N:  #끝까지 탐색했으면 완전한 해를 찾은것이므로 경우의 수 카운트 세아리기
        global total_cnt

        total_cnt += 1

    else:
        for i in range(N):
            if visited[i]:  #만약 앞에 다 방문했다고 되어있으면 다음 i 값으로 넘어가기
                continue
            
            board[n] = i

            if check(n):
                visited[i] = True
                queen(n+1)
                visited[i] = False  #이렇게 해줘야 그 다음 경우의수를 구할때 False로 인식하여 새로운 경우의수를 찾을 수 있음


def check(n):
    for i in range(n):  # 같은 열에 있거나 대각선에 위치할때..
        if (board[n] == board[i]) or (n - i == abs(board[n]-board[i])):
            return False
    return True


queen(0)
print(total_cnt)