n= int(input())

m = int(input())

ary = [0] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())

    for r in range(x,y):
        ary[r] = 1


print(ary.count(0) - 1)