from collections import Counter
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
	n = int(input())
    
	ary = list(map(int, input().split()))
	most_num = Counter(ary).most_common()[0][0]
	print("#" + str(i),str(most_num))