ary = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(ary)):
    min_idx = i ## 가장 작은 원소의 인덱스

    for j in range(i+1, len(ary)): # 기준이 되는 인덱스 이후의 데이터들
        if ary[j] < ary[min_idx]:
            min_idx = j ## 이렇게 해야 다음 행에서 정렬 할 수 있음 (자리 위치 변경)

    ary[i], ary[min_idx] = ary[min_idx], ary[i]

print(ary)