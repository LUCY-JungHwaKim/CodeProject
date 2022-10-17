import sys
N = int(sys.stdin.readline()) ## 입출력 시 시간 줄여줌
N_stack = []
while N > 0:
    exe_str = sys.stdin.readline().split()

    if exe_str[0] == 'push': # push 일때 stack 넣어줌
        N_stack.append(int(exe_str[1]))
        #print(int(exe_str.split(' ')[1]))
    if exe_str[0] == 'pop':
        if len(N_stack) == 0:
            print(-1)
        else:
            print(N_stack.pop()) #제일 상위꺼 pop
    elif exe_str[0] == 'top':
        if len(N_stack) == 0:
            print(-1)
        else:
            print(int(N_stack[-1])) # 제일 끝에꺼 출력
    elif exe_str[0] == 'size': # 길이 출력
        print(len(N_stack))
    elif exe_str[0] == 'empty': # 길이 확인하면 됨
        if len(N_stack) == 0:
            print(1)
        else:
            print(0)

    N -= 1