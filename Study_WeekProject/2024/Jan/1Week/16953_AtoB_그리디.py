n,m = map(int, input().split())

## 곱하기 2는 나누기 2로
## 1을 오른쪽에 추가하는건 반대로 1을 빼서 10으로 나눈 몫임

cnt = 0

while m != n and m > 0:



    if (m % 10) == 1: ## 이 조건을 해줘야함 단순이 홀짝인지만 확인하면 안됨
        ## 그리고 큰 수부터 나눠줘야함, 그리디 만족
        m = int((m-1)//10)
        cnt += 1

    elif m % 2 == 0: ## 먼저 2로 나눠 떨어지는지 확인
        m = int(m // 2)
        cnt += 1

    else:
        cnt = -1
        break

if m != n: ## 결과적으로 n이랑 같지 않을땐 -1
    print(-1)
else:
    print(cnt + 1)