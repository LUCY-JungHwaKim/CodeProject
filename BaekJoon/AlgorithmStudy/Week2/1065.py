N = int(input())

cnt = 0
for i in range(1,N+1):
    num_list = list(map(int, str(i)))
    dif_ary = []
    for j in range(len(num_list)-1):
        dif_ary.append(num_list[j+1]-num_list[j])
    
    if len(set(dif_ary)) == 1:
        cnt += 1
    if i < 10:
        cnt += 1
print(cnt)