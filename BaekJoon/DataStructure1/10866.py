import sys
from collections import *
N = int(sys.stdin.readline()) ## 입출력 시 시간 줄여줌
N_stack = deque()
while N > 0:
    exe_str = sys.stdin.readline().split()

    if exe_str[0] == 'push_front': # 맨앞쪽에 입력할땐 appendleft
        N_stack.appendleft(int(exe_str[1]))
        #print(int(exe_str.split(' ')[1]))
    elif exe_str[0] == 'push_back': # 뒤에서 입력할땐 pop
        N_stack.append(int(exe_str[1]))
        #print(int(exe_str.split(' ')[1]))
    elif exe_str[0] == 'pop_front': ## 맨 뒤에꺼 출력
        if len(N_stack) == 0:
            print(-1)
        else:
            print(N_stack.popleft()) #제일 앞에꺼 pop
    elif exe_str[0] == 'pop_back':
        if len(N_stack) == 0:
            print(-1)
        else:
            print(N_stack.pop()) #제일 앞에꺼 pop
    elif exe_str[0] == 'size': # 길이 출력
        print(len(N_stack))
    elif exe_str[0] == 'empty': # 길이 확인하면 됨
        if len(N_stack) == 0:
            print(1)
        else:
            print(0)
    elif exe_str[0] == 'front':
        if len(N_stack) == 0:
            print(-1)
        else:
            print(N_stack[0])
    elif exe_str[0] == 'back':
        if len(N_stack) == 0:
            print(-1)
        else:
            print(N_stack[-1])

    N -= 1