N,k =  map(int, input().split())
from collections import deque
## 원을 이루고 있다 --> 거의 deque 문제일 가능성 높음

circle = deque(i+1 for i in range(N)) #설정된 N만큼 값부여
result_lst = []

while len(circle) != 0:
    rot = -(k-1)
    ## rotate(-2) 면은 1,2,3,4,5가 있을때
    ## 3,4,5가 됨
    ## 2면은 4,5,1,2,3 이렇게 됨
    circle.rotate(rot)
    result_lst.append(circle.popleft())
    ## 돌려주고 맨 앞에 있는게 제거 되므로 
    ## 제거하는 요소를 결과 리스트에 넣어줌

result_lst = str(result_lst)
result_lst = result_lst.replace('[', '<')
result_lst = result_lst.replace(']', '>')
## 출력을 위해 결과 리스트를 str로 바꿔주고
## 필요한 문자열을 변경해줌
print(result_lst)











