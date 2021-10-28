n, m = map(int, input().split())

n , m = list(str(n)), list(str(m))

new_n = ""
new_m = ""
for i in range(2,-1,-1):
    new_n += n[i]
    new_m += m[i]

if int(new_m) > int(new_n):
    print(new_m)
else:
    print(new_n)