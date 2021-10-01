
a,b = map(int, input().split())


divisor_list = list(filter(lambda y : a%y == 0 ,list(range(1,a+1))))

if len(divisor_list) < b:
    print(0)
else:
    print(divisor_list[b-1])
