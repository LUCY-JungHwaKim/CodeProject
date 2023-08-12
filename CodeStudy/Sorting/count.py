ary = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

cnt = [0] * (max(ary) + 1)
## 데이터 길이 1보다 많게 리스트 선언

for i in range(len(ary)):
    cnt[ary[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가
    
for i in range(len(cnt)): ## 리스트에 기록된 횟수만큼 출력
    for j in range(cnt[i]): 
        print(i, end = ' ')
