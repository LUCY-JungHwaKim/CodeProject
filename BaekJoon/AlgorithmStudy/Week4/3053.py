from math import pi
R = int(input())



print("{:.6f}".format(pi*(R**2)))
print("{:.6f}".format(2*(R**2)))



#택시기하학에서의 원은 마름모꼴이라고함
#반지름이 R을 기준으로 햇을 때
#R*R*0.5 = 삼각형 하나에 대한 넓이
#근데 마름모꼴이면 삼각형이 네개니깐 *4하면 2*R^2가 나옴
#https://ahdelron.tistory.com/41?category=932238