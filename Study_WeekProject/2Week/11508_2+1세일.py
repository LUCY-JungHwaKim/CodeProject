import sys

n = int(input())

lst = []

for i  in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
print(lst)
nums = len(lst) // 3
#print(nums)
result=0

for m in range(nums+1):
    strt = (m*3)
    end = (m*3)+3
    chk = lst[strt:end]
    #print(chk, strt, end)
    if len(chk) == 3:
        result += sum(chk[:2])
    else:
        result += sum(chk)
print(result)
