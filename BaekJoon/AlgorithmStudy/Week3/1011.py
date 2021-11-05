import math

T = int(input())
result_ary = []

for _ in range(T):
    start, end = map(int, input().split())

    distance = end-start
    n = round(math.sqrt(float(distance)))   #가장 가까운 제곱근 찾기
    #루트 씌워서 반올림 
    #n이라는게 총 이동횟수를 뜻함
    #아래 if문에 해당되는것이 최소 이동횟수인 경우의 규칙을 나타냄

    while True:
        if abs(n**2 - distance) <= n:
            if distance <= n**2 :
                result_ary.append(2*n-1)
                break
            else:
                result_ary.append(2*n)
                break

for i in range(len(result_ary)):
    print(result_ary[i])


#distance   총 이동횟수
#3  3
#4  3
# 5   4
# 6   4
# ----------- 4 (2*n)
# 7   5   
# 8   5
# 9   5
# 10  6
# 11  6
# 12  6
# -------------6
# 13  7
# 14  7
# 15  7   
# 16  7
# 17  8
# 18  8
# 19  8  
# 20  8
# -----------8