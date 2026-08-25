# [프로그래머스 12909] 올바른 괄호 풀이

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909
- 사용 언어: python
- 예상 유형(자동 감지): BFS, 스택/큐
- 원본 코드: `프로그래머스/8m:4w/12909_2.py`
- 생성일: 2026-08-24

## 문제 설명

> 올바른 괄호
>
> (자세한 문제 설명 및 제약 조건은 위 링크를 참고해주세요.)

## 접근 방법

아래는 코드 패턴을 정규식으로 훑어 **추정**한 알고리즘 유형입니다.
실제 풀이 논리와 다를 수 있으니 확인 후 자연어로 다듬어서 채워주세요.

- BFS(너비 우선 탐색)를 활용하는 것으로 보입니다.
- 스택 또는 큐 자료구조를 활용하는 것으로 보입니다.

**TODO:** 문제를 어떻게 접근했는지, 핵심 아이디어와 시행착오를 여기에 직접 적어주세요.
(예: 처음에 어떤 방법을 시도했다가 왜 실패했는지, 최종적으로 어떤 아이디어로 풀었는지)

## 코드

```python
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

from collections import *


def solution(s):
    answer = True

    queue = deque()
    cur_s = ""

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
```

## 시간복잡도

**TODO:** 시간/공간 복잡도를 적어주세요.

## 회고

**TODO:** 풀면서 배운 점, 실수했던 부분, 다음에 비슷한 문제를 만나면 어떻게 할지 적어주세요.

---
*이 글은 push 시 자동으로 생성된 초안입니다. 티스토리에 올리기 전에 위 TODO 항목들을 채우고 자유롭게 다듬어주세요.*
