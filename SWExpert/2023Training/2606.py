n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]

#print(arr)


visited = [0 for i in range(n+1)]

## 그래프 생성
for i in range(m):
    a,b = map(int, input().split())
    arr[a].extend([b])
    arr[b].extend([a])

def dfs(start):
    visited[start] = 1

    for nx in arr[start]:
        if visited[nx] == 0: # 방문안했으면 가는거임
            dfs(nx) ## 재귀방법

dfs(1)
print(sum(visited)-1) ## 1번 컴퓨터 방문을 빼줘야함