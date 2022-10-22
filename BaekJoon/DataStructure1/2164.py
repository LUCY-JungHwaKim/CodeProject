N= int(input())
from collections import deque

circle = deque(i+1 for i in range(N))

while len(circle) != 1:

    circle.popleft() # 가장 왼쪽에 있는 요소 pop
    circle.rotate(-1) # 제일 뒤로 보내기

print(circle.popleft())