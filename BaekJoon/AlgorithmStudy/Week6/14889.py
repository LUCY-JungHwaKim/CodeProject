import sys
N = int(input())

total_data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#zeros_loc = [(i,j) for i in range(9) for j in range(9) if total_data[i][j] == 0]
person_idx = [i+1 for i in range(N)]

lst = []
partial_lst = []
min_dif = 99999

partial_sum = 0
def partial_find_pair(cnt, idx, length, lst):
    global partial_sum
    if cnt-1 == 2:
        i,j = partial_lst[0]-1, partial_lst[1]-1
        #print(" ".join(map(str, partial_lst)))
        
        return total_data[i][j]

    else:
        
        for i in lst:
            if i not in partial_lst:
                partial_lst.append(i)
                value = partial_find_pair(cnt+1, i, length, lst)
                
                if value != None:
                    partial_sum += value
                partial_lst.pop()
        
        # print(partial_sum)
        

def find_pair(cnt, idx):
    global partial_sum, min_dif
    if cnt-1 == (N//2):
        #print(" ".join(map(str, lst)) + "----------")
        partial_sum = 0
        #---점수계산--#
        if len(lst) == 2:
            remain_ary = list(set(person_idx)-set(lst))
            i,j = lst[0]-1, lst[1]-1
            x,y = remain_ary[0]-1, remain_ary[1]-1
            start_score = total_data[i][j] + total_data[j][i]
            link_score = total_data[x][y] + total_data[y][x]
            if abs(start_score-link_score) < min_dif:
                min_dif = abs(start_score-link_score)
            
            return
            #calculate_score()
        elif len(lst) > 2:
            remain_ary = list(set(person_idx)-set(lst))
            partial_find_pair(1,1,len(lst), lst)
            start_score = partial_sum
            partial_sum = 0
            partial_find_pair(1,1, len(remain_ary), remain_ary)
            link_score = partial_sum
            if abs(start_score-link_score) < min_dif:
                min_dif = abs(start_score-link_score)
        return
    
    else:

        for i in range(idx,N+1):
            if i not in lst:
                lst.append(i)
                find_pair(cnt+1, i)
                lst.pop()

find_pair(1,1)
print(min_dif)