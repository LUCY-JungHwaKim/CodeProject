x = int(input())
## 보텀업 방식으로 진행

d = [0] * 30001
## 호출 횟수 저장
## 1일때는 연산 진행 안해도 되므로 함수 호출 X ==> 0
## 2일때는 2로 나누거나, 1을 빼주면 됨 호출 횟수 = 1

for i in range(2, x+1):
    #먼저 현재의 수에서 1을 빼줌
    d[i] = d[i-1]+1
    ## +1은 호출 횟수를 구해야 하기 때문
    ## 항상 호출횟수가 더 작은거를 저장하도록 해야 함
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
        ## 호출 횟수 더 작은거 출력
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])