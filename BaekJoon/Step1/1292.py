start, end = map(int, input().split())

num_ary = []

for i in range(1000):
    for j in range(i):
        num_ary.append(i)
#print(num_ary)
print(sum(num_ary[start-1:end]))