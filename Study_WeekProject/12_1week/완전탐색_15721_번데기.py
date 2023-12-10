from collections import deque
import sys
import io
n = int(input()) ## 사람 수
m = int(input()) ## 몇번째
s = int(input()) ## 0: 번, 1:데기

pers_q = [i for i in range(n)] ## 사람 큐
pers_q = deque(pers_q)
#print(pers_q)
#pers_q.rotate(-1) ## 시계 반대방향으로 굴리는거임
#print(pers_q)

n = 1
totalstr = []
b_cnt = 0
d_cnt = 0
result = 0
check_exit = 0
while True:
    strary = ['b', 'd', 'b', 'd']
    b_str = ['b'   for _ in range(n + 1)]
    d_str = ['d' for _ in range(n + 1)]

    totalstr = deque(strary + b_str + d_str)

    while totalstr:
        now_c = totalstr.popleft() ## 현재 꺼 출력

        if now_c == 'b':
            b_cnt += 1
            if (s == 0) & (b_cnt == m):
                result = pers_q[0] ## 현재 사람 출력
                check_exit = 1 # 탈출조건
                break
        else:
            d_cnt += 1
            if (s == 1) & (d_cnt == m):
                result = pers_q[0] ## 현재 사람 출력
                check_exit = 1  # 탈출조건
                break

        pers_q.rotate(-1)

    if check_exit == 1:
        break

    n += 1

print(result)