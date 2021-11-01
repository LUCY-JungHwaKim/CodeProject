M = int(input())
N = int(input())


minor_list = []


for i in range(M, N+1):
    minor_cnt = 0
    for j in range(i):
        if int(i%(j+1)) == 0:   #나누었을때 자기 자신과 1밖에 없을때 소수 취급
            minor_cnt += 1     
            if minor_cnt > 2:
                break
    if minor_cnt == 2:
        minor_list.append(i)

            

if len(minor_list) == 0:
    print("-1")
else:
    print(sum(minor_list))
    print(min(minor_list))
