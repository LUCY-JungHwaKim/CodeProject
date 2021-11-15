import collections
T = int(input())

N_ary = []
for i in range(T):
    N_ary.append(int(input()))

N_ary = sorted(N_ary)
print(round(sum(N_ary)/len(N_ary)))
median_idx = int(len(N_ary)/2)
print(N_ary[median_idx])

counts = collections.Counter(N_ary)
order = counts.most_common()
maximum = order[0][1]


modes = []
for num in order:
    if num[1] == maximum:
        modes.append(num[0])

if len(modes) > 1:
    print(modes[1])
else:
    print(order[0][0])

print(max(N_ary)-min(N_ary))