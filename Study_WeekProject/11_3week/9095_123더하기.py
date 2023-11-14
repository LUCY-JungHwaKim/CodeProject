n = int(input())
n_lst = []
for i in range(n):
    num = int(input())
    n_lst.append(num)
max_num = max(n_lst)
sumlst = [0 for _ in range(max_num+1)]

#print(max_num, sumlst)

sumlst[1] = 1
sumlst[2] = 2
sumlst[3] = 4

for i in range(4, max_num+1):
    sumlst[i] = (sumlst[i-1] + sumlst[i-2] + sumlst[i-3])

for i in range(n):
    idx = n_lst[i]
    print(sumlst[idx])