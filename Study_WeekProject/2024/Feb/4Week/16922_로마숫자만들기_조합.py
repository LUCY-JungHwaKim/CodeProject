n = int(input())
from itertools import permutations, combinations
#

#lst = [1, 5, 10, 50]
sumlist = [0] * (1001)
numlst = [1,5,10,50]


rsltary = []

def dfs(depth, num):
    global rsltary

    if depth == n:
        sumlist[sum(rsltary)] = 1
        #print(sol)
        # sum = 0
        # for x in sol:
        #     sum += dict[x]
        # rsltary.append(sum)

        return

    for i in range(num, 4):
        rsltary.append(numlst[i])
        dfs(depth + 1, i)
        rsltary.pop()



dfs(0,0)
print(sum(sumlist))
# print(len(set(rsltary)))