n,k = map(int, input().split())
lst = []

for i in range(n):
    lst.append(int(input()))
idx = n-1
cnt = 0

while k > 0:

    if lst[idx] <= k: ## k보다 동전 수가 더 크면 계산 X
        cnt += (k // lst[idx]) ## k를 동전 가치로 나눈 것의 몫이 사용할 수 있는 동전 개수

        cur_n = k % lst[idx] ## 그거에 대한 나머지가 다음 k 값이 됨
        k = cur_n

    idx -= 1 ## 뒤에서부터 시작이므로 1씩 빼주면 됨

print(cnt)