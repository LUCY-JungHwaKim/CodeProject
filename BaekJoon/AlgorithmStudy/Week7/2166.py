import sys

N = int(sys.stdin.readline())

x_ary = []
y_ary = []

for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    x_ary.append(x)
    y_ary.append(y)


#신발끈정리 사용 (점의 좌표가 주어지면 해당 공식을 통해 다각형의 넓이를 구할 수 있음)
#만약 꼭짓점이 세개를 제공한다면
#x1y2+x2y3+x3y1-x2y1-x3y2-x1y3
#이렇게 구한 후에 절댓값을 취해서 2로 나누는거임
#각자 해서 절댓값 취하는게 절대 아님


answer = 0

for i in range(N-1):
    answer += ((x_ary[i]*y_ary[i+1])-(x_ary[i+1]*y_ary[i]))

answer += ((x_ary[N-1]*y_ary[0])-(x_ary[0]*y_ary[N-1]))

answer = round(abs(answer/2), 1)

print(answer)