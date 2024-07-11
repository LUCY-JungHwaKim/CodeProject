import sys
sys.setrecursionlimit(10**9)

def dfs(x, value):

    for i in dictary[x]:
        a,b = i ## 여기 안에 두개의 원소를 가진 리스트니깐
        if dist[a] == -1: ## 방문한 곳이 아니라면
            dist[a] = value + b ## 거리 더하기
            dfs(a, value+b)


 
if __name__ == "__main__":

    n = int(input())

    dictary =  {i: [] for i in range(1, n + 1)}

    for _ in range(n-1):
        e1, e2, k = map(int, input().split()) ## 간선 두개, 그리고 가중치   

        dictary[e1].append([e2, k])
        dictary[e2].append([e1, k])
        ## 삽입까지는 맞게 했는뎅..



    ## 루트(1번 노드)에서 가장 먼 곳을 찾음
    dist = [-1] * (n+1) ## 거리 
    dist[1] = 0 ## 루트 노드니깐
    dfs(1,0)

    ## 먼곳을 찾은 노드에 대해서 가장 먼 노드를 찾음 --> 그 두점이 지름임 (어렵다 헉스)
    start = dist.index(max(dist))
    dist = [-1] * (n+1) ## 다시 재 초기화
    dist[start] = 0
    dfs(start, 0)

    print(max(dist)) ## 지름 값 :  max 가져오기


    ## Ref : https://kyun2da.github.io/2021/05/04/tree's_diameter/
