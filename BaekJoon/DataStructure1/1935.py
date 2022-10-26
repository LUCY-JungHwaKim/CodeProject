##후위표기식 : 35+와 같이 연산자가 피연산자 뒤에 있는 표기식
##https://woochan-autobiography.tistory.com/786
## 352*+ ==> 3+5*2
## (수정중..)
import sys
N = int(input())
str_ipt = list(str(input()))

##https://velog.io/@dailyhyun/BOJ%EB%B0%B1%EC%A4%80-1935.-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D2

num_lst = []

for i in range(N):
    ipt = int(input())
    num_lst.append(ipt)

rslt_stack = []
opt_lst = ['*', '+', '/', '-']
for i in range(len(str_ipt)):
    if str_ipt[i] not in opt_lst:
        rslt_stack.append(str_ipt[i])
    else:
        num1 = rslt_stack.pop()
        num2 = rslt_stack.pop()
        rslt_num = 0

        if str_ipt[i] == '*':
            rslt_num = num1*num2
        elif str_ipt[i] == '+':
            rslt_num = num1+num2
        elif str_ipt[i] == '/':
            rslt_num = round(num1/num2, 2)
        elif str_ipt[i] == '-':
            rslt_num = num1-num2

        rslt_stack.append(rslt_num

print(rslt_stack)