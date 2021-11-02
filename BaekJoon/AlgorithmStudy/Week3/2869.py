import math
A,B,V = map(int, input().split())

#하루 = 낮+밤
#낮에는 +A, 밤에는 -B
#하루에(A-B)만큼 올라감

if (A-B) >= V:
    print(1)
else:
    day = (V-B)/abs(A-B)
    print(math.ceil(day))   #올림하는 함수

