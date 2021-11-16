#DFS - stack, recursive -- 여기서 stack은 주로 list로 사용
#DFS는 마지막에 입력된게 제일 처음으로 나옴 즉, LIFO --> 그래서 list.pop()이런식으로 맨 마지막 요소 pop해야함

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def dfs_stack(graph, start):
    visited = {}
    stack = []

    stack.append(start)

    while stack:    #stack이 차있는 동안은 계속 while문 반복
        current = stack.pop()   #마지막에 입력된 요소 pop

        if current not in visited:  #꺼낸 요소가 visited 리스트에 없으면은
            visited[current] = True #현재 꺼낸 요소를 visited에 삽입
            stack.extend(graph[current])    #현재 꺼낸 요소와 연결된 노드 스택에 삽입

    return list(visited.keys()) #visited를 dictionary 형태로 저장 O(1) -> list로 저장하는게 시간복잡도 더 걸림 O(n)




recursive_visit = {}    #재귀 함수를 호출하니깐 재귀함수의 visited행렬은 함수 외부에 선언
def dfs_recursive(graph, start):

    if start in recursive_visit:    #이미 방문한 노드면 탐색 종료
        return
    
    recursive_visit[start] = True

    for node in graph[start]:   #재귀 호출
        dfs_recursive(graph, node)
    


print(dfs_stack(graph, 'A'))    #Stack ==> LIFO
print(dfs_recursive(graph, 'A'))    #재귀 ==> 현재 노드서 갖고오니깐 LIFO 아님
print(list(recursive_visit.keys()))
#이후에 전위순회, 중위순회, 후위 순회 서치
#dfs --> 기본적으로 전위순회
#전위 순회 --> 부모, 좌, 우
#중위 순회 --> 좌, 부모, 우
#후위 순회 --> 좌, 우, 부모

