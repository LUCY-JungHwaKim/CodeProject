n,m = map(int, input().split())

graph = []
for i in range(n): ## 이미 여기서 stack, list 만든거임
    graph.append(list(map(int, input()))) ## split을 안하면 입력할때 띄어쓰기로 입력 안해도 됨

## 재귀로 푸니깐 굳이 pop같은거 안해도 됨

print(graph)

result = 0

def dfs(x,y):
    
    if x>= n or x < 0 or y >= m or y <0:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False ## 종료


for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)