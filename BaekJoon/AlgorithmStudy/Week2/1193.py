N = int(input())

num = 1
line = 1
while N > line:
    N -= line
    line += 1   

if line%2 == 0: #짝수는 아래대각선방향으로
    a = N
    b = line-N+1
else:       #홀수는 위대각선방향으로
    a = line-N+1
    b = N

print(str(a) + '/' + str(b))