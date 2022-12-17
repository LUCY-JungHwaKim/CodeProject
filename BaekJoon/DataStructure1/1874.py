import sys
N = int(sys.stdin.readline()) ## 입출력 시 시간 줄여줌
num_lst = [int(sys.stdin.readline()) for i in range(N)]
num_srt = [i for i in range(N,0,-1)]

#print(num_lst, num_srt)
stack_lst = [] # 스택
op_lst = [] # 연산자 리스트

og_idx = 0 # 원래 기존 리스트의 idx

## 리스트내에서 검사할 때 list.count하면 너무 오래 걸릴 수도 있음
## 시간복잡도 두 배 이상 걸릴 수도 있음

for i in range(num_lst[0]):
    stack_lst.append(num_srt.pop())
    op_lst.append('+')

while og_idx < N:
    if (not stack_lst) or (stack_lst[-1] != num_lst[og_idx]) :
        if num_srt:
            stack_lst.append(num_srt.pop())  ## 일단 넣기
            op_lst.append('+')
        else:
            break
    else:
        ## 마지막에 넣은게 스택 끝값과 같으면 pop
        stack_lst.pop()
        op_lst.append('-')
        og_idx += 1
#print(op_lst)
if og_idx == N:
    sys.stdout.write('\n'.join(op_lst))
else:
    sys.stdout.write('NO')