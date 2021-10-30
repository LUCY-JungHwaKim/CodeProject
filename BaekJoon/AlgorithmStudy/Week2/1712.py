A,B,C = map(int, input().split())

count = 1

if B<C:
    print(int(A/(C-B)   ) + 1)
else:
    print(-1)
