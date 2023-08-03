ary = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(ary)):
    for j in range(i, 0, -1): # 기준이 되는 인덱스 이후의 데이터들
        if ary[j] < ary[j-1]: ## 왼쪽으로 이동해야하는 경우
            ary[j], ary[j-1] = ary[j-1], ary[j]
        else:## 자기보다 작은 데이터 발견하면 현재 그자리에서 멈추기!!!
            break


print(ary)