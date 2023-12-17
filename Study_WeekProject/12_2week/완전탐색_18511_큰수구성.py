n, k = map(int, input().split())
ary = list(map(int, input().split()))
max_sum = -999999
n_lnt = len(str(n))

def dfs(ary, sol):
    global max_sum
    #print(sol)

    if len(sol) > n_lnt:
        return

    if len(sol) > 0:
        num_str = int(''.join(map(str, sol)))

        if (num_str <= n) & (num_str >= max_sum):
            max_sum = num_str

    for i in range(k):
        sol.append(ary[i])
        dfs(ary, sol)
        sol.pop()

# numbers = [1, 2, 3]
# string_numbers = ''.join(str(num) for num in numbers)
# print(string_numbers)  # 결과: "123"

dfs(ary, [])
print(max_sum)
#
#
# from itertools import product
#
# n, k_num = map(int, input().split())
# len_max = len(str(n))
# k = list(input().split())
#
# while True:
#     tmp = list(product(k, repeat=len_max))  # repeat를 통해 몇 개를 뽑을지 결정
#     result = []
#
#     for i in tmp:
#         if int("".join(i)) <= n:
#             result.append(int("".join(i)))
#
#     if len(result) >= 1:
#         print(max(result))
#         break
#
#     else:
#         len_max -= 1