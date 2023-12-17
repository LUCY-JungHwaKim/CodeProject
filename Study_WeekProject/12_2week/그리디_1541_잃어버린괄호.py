import sys

ary = sys.stdin.readline()

min_sp = ary.split('-')

plu_m = 0
#print(min_sp)

for i in min_sp[0].split('+'):
    plu_m += int(i)

for i in min_sp[1:]:
    for j in i.split('+'):
        plu_m -= int(j)


print(plu_m)

# for i in range(len(min_sp)):
#     print(min_sp[i])
#     plu_sp = min_sp[i].split('+')
#     print(plu_sp)
#
#     for j in range(len(plu_sp)):
#         plu_m