totalinp = []

while True:
    inp = list(map(int, input().split()))
    totalinp.append(inp)
    if inp[0] == 0: ##  0 누르면 종료
        break


def dfs(k, graph, idx, sol):
    #print(sol)

    if len(sol) == 6:
        print(*sol)
        return


    for i in range(idx, len(graph)):
        sol.append(graph[i])
        dfs(k, graph, i+1, sol)
        sol.pop()




for i in range(len(totalinp)):
    dfs(totalinp[i][0], totalinp[i][1:], 0, [])
    print("")