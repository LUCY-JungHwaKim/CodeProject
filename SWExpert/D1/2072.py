T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    total_sum = 0
    input_nums = map(int, input().split())
    for inputs in input_nums:
        if inputs % 2 != 0:
            total_sum += inputs
    print("#" + str(test_case) + " " + str(total_sum))