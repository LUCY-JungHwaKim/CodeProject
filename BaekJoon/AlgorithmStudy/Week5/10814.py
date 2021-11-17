import sys
import operator
T = int(sys.stdin.readline())

person = []
for i in range(T):
    person.append(list(sys.stdin.readline().split()))

person.sort(key = lambda x:int(x[0]))    #나이를 기준으로 정렬..
#어렵구만..



for i in person:
    print(i[0], i[1])
