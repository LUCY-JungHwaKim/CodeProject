from collections import deque

n, m = map(int, input().split())

timecnt = 0

q = deque()

visited = [-1 for _ in range(100001)]
visited[n] = 0

q.append(n)  ## 내가 너무 어렵게 생각한듯..

while q:
    s = q.popleft()
    if s == m:
        print(visited[s])  ## 방문 배열에 저장된 값 출력
        break

    if 0 <= s - 1 < 100001 and visited[s - 1] == -1:  ## -1 할 때
        visited[s - 1] = visited[s] + 1
        q.append(s - 1)

    if 0 <= s * 2 < 100001 and visited[s * 2] == -1:  ## *2 할 때
        visited[s * 2] = visited[s]
        q.append(s * 2)

    if 0 <= s + 1 < 100001 and visited[s + 1] == -1:  ## +1 할 때
        visited[s + 1] = visited[s] + 1
        q.append(s + 1)