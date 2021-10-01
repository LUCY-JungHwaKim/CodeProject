import sys
max_ans, min_ans = -sys.maxsize -1, sys.maxsize

N = int(input())
input_num = list(map(int, input().split()))
plus, minus, multiply, divide = list(map(int, input().split()))

def recursive_function(arg_input, idx, arg_plus, arg_minus, arg_multiply, arg_divide):
    global max_ans, min_ans

    if idx == N:
        max_ans = max(max_ans, arg_input)
        min_ans = min(min_ans, arg_input)
        return

    if arg_plus > 0:
        recursive_function(arg_input + input_num[idx], idx+1, arg_plus-1, arg_minus, arg_multiply, arg_divide)
    if arg_minus > 0:   #elif가 아닌걸 기억하기
        recursive_function(arg_input - input_num[idx],  idx+1, arg_plus, arg_minus-1, arg_multiply, arg_divide)
    if arg_multiply > 0:
        recursive_function(arg_input * input_num[idx],  idx+1, arg_plus, arg_minus, arg_multiply-1, arg_divide)
    if arg_divide > 0:
        recursive_function(int(arg_input / input_num[idx]),  idx+1, arg_plus, arg_minus, arg_multiply, arg_divide-1)


recursive_function(input_num[0], 1, plus, minus, multiply, divide)
print(max_ans)
print(min_ans)


