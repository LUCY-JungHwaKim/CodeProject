mg = input()

mg_max = []
mg_min = []
#print(mg.split('K'))
for mword in mg.split('K'):
    #print(mword)
    if mword:
        mg_min.append(str(10**(len(mword)-1)))
        mg_max.append(str(5*10**(len(mword))))
    else :
        mg_min.append('')
        mg_max.append(str(5))
    #print(mg_max)
#print('1'*(len(mg_max[-1])-1))
print(''.join(mg_max[:-1])+'1'*(len(mg_max[-1])-1))
print('5'.join(mg_min))