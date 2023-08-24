n,m = map(int, input().split())
ar = []
for i in range(n):
    ar.append(int(input()))

d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(ar[i], m+1):
        ##  화폐 단위부터 끝까지 계속 연산해 가면서 최소 화폐 개수를 저장할 수 있도록 하기
        if d[j - ar[i]] != 10001:## 화폐 단위들을 빼줌..
            ## 즉, a2, a3이런 값들이 존재하는 경우
            d[j] = min(d[j], d[j-ar[i]] + 1)

if d[m] == 10001: ## 답이 없다면, 방법이 없다면
    print(-1)
else:
    print(d[m])