##그리디
#from collections import deque
str_inp = str(input())
#
#
str_inp = str_inp.replace('XXXX', 'AAAA')
str_inp = str_inp.replace('XX', 'BB')

if 'X' in str_inp:
    print(-1)
else:
    print(str_inp)

