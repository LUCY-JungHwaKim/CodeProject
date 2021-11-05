import math

T = int(input())
result_ary = []

for _ in range(T):
    start, end = map(int, input().split())

    distance = end-start
    n = round(math.sqrt(float(distance)))
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