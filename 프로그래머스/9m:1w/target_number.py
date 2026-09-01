## https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return

        dfs(index + 1, current_sum + numbers[index])  # 값을 더한 경우

        dfs(index + 1, current_sum - numbers[index])  # 값을 뺀 경우

    dfs(0, 0)

    return answer