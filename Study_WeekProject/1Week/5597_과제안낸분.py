# 어차피 학생은 최대 30명..

check = [0] * 31
# 0번째 제외

for i in range(28): ## 제출안한 2명 찾는 거기 때문에 28까지 입력
    n = int(input())
    check[n] = 1

## 너무 간단하게 풀어버림..
for j in range(1, len(check)):
    if check[j] == 0:
        print(j)