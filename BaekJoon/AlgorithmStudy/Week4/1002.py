
T = int(input())
#터렛이 동그라미형태로 공격하는 거임
#게임을 잘 몰라서 첨에 이해하기 어려웠음
result = []
for i in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())

    distance = ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5
    radian = [r_1, r_2, distance]
    max_r = max(radian)
    radian.remove(max_r)
    #두 원의 교점을 구하는거임
    if distance == 0:   #거리가 0일때
        if r_1 == r_2:  #원이 일치할때
            result.append("-1")
        else:   #크기가 다를때
            result.append("0")
    else:   #거리가 0 이아닐때 
        if max_r == sum(radian) or distance == r_1 + r_2:
            result.append("1")  #교점 1개
        elif max_r > sum(radian):
            result.append("0")  #교점 없음
        else:   #교점 2개
            result.append("2")


for i in range(len(result)):
    print(result[i])
    
#https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-1002-Python-%ED%84%B0%EB%A0%9B