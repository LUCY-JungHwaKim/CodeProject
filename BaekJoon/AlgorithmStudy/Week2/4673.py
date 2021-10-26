num_ary = [i+1 for i in range(10000)]
result_ary = []

idx = 0

for i in range(10000):
    
    num = sum(map(int, str(i+1))) + i + 1

    #print(sum(map(int, str(i+1))))
    if  num in num_ary and num <= 10000 :
        #print(num,i+1)
        result_ary.append(num)

result_ary = set(result_ary)

for i in sorted(set(num_ary)-result_ary):
    print(i)

#기억하면 좋을 코드
#set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용된다고 함