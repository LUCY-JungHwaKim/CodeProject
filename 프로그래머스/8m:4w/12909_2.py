# https://school.programmers.co.kr/learn/courses/30/lessons/12909

from collections import *


def solution(s):
    answer = True

    queue = deque()
    cur_s = ""
    cur_b = "d"

    for idx, i in enumerate(list(s)):
        if (i == ")") & (idx == 0):
            return False
        elif i == "(":
            queue.append(i)
            cur_s = i
        else:
            if (len(queue) > 0) & (cur_s == "("):
                queue.pop()

    if len(queue) == 0:
        return True
    else:
        return False