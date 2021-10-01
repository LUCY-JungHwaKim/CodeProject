tall_ary = []
result_ary = []
for i in range(9):
    tall_ary.append(int(input()))

for i in range(9):
    for j in range(9):
        result_ary = tall_ary.copy()
        if i != j:
            result_ary.remove(tall_ary[i])
            result_ary.remove(tall_ary[j])
            if sum(result_ary) == 100:      
                result_ary = sorted(result_ary)
                for m in range(len(result_ary)):
                    print(result_ary[m])
                exit()
            
