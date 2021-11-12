import math
from collections import deque

def solution(progresses, speeds):
    answer = [0 for _ in range(len(progresses))]
    work = deque()
    
    for i in range(len(progresses)):
        remain_work = math.ceil((100-progresses[i])/speeds[i])
        work.append(remain_work)

    print(work)
    work_len = len(work)
    max_num = work.popleft()
    cnt = 0
    answer[cnt] += 1

    while len(work) > 0:
        current = work.popleft()
        
        if current <= max_num:  #해야하는 일 수가 같을 때도 포함해줘야함
            
            answer[cnt] += 1
        else:
            cnt += 1
            answer[cnt] = 1
            max_num = current   #최대값 설정 해줘야함

    answer = list(filter(lambda x: x > 0, answer))
        
    return answer

print(solution([95,95,95,95], [4,3,2,1]))