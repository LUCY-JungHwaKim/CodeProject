
from itertools import combinations

n, m = map(int, input().split())
ice_ary = [[False for _ in range(n)] for _ in range(n)]

## 내가 너무 어렵게 생각했다
## 시간 초과 문제를 고려했어야 했는데
## 그리고 단순 숫자면 그냥 dfs로 구현을 안해도 된다

for i in range(m):
    a,b = map(int, input().split())
    ice_ary[a-1][b-1] = True
    ice_ary[b- 1][a - 1] = True ## 이걸 해야 맞다고 함..흠
    ## combination이 원소의 순서를 고려하지 않고 조합을 생성하기 때문에 양방향 체크를 해야 한대


rslt = 0
for i in combinations(range(n),3):
    ## 어차피 조합은 무조건 세개임
    if ice_ary[i[0]][i[1]] or ice_ary[i[0]][i[2]] or ice_ary[i[1]][i[2]]:
        ## 조합 세개가 있을 때 그 중에서 두 개 원소들만 조합하면 안되는 집합에 포함되는지 확인하면 되니깐
        continue

    rslt += 1

print(rslt)

