# [프로그래머스 43165] 타겟 넘버

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
- 사용 언어: Python
- 문제 유형: DFS / 재귀
- 원본 코드: `프로그래머스/9m:1w/target_number.py`

## 💡 접근 방법

- 인덱스별로 재귀 호출해 현재 합을 누적함
- 각 원소에 대해 더하는 경우와 빼는 경우 두 갈래로 재귀 분기함
- 모든 원소를 처리한 시점에서 목표값과 비교해 카운트 증가함

### 📌 핵심 아이디어

각 숫자에 대해 + 또는 - 두 가지 선택을 재귀적으로 모두 탐색해 모든 부호 조합의 합을 계산하고 목표값과 일치하는 경우를 셈함

## 💻 코드

```python
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
```

## ⏱️ 시간 · 공간 복잡도

- **시간복잡도: `O(2^N)`**
  - 각 원소마다 두 갈래로 분기되어 총 호출 수가 대략 2^N(리프 수) 수준이고 각 호출은 상수 시간 작업만 수행함
- **공간복잡도: `O(N)`**
  - 재귀 호출의 최대 깊이가 numbers의 길이 N에 비례해 호출 스택을 O(N)만큼 사용함

## 🔎 코드 리뷰

### 잘 적용한 부분

- 문제가 요구하는 모든 경우를 명확하고 간결하게 완전탐색으로 구현함
- 추가 자료구조 없이 현재 합을 인자로 전달해 메모리 오버헤드 최소화함
- 종료 조건과 카운트 증가 로직이 명확하게 분리되어 가독성 높음

### 🔧 개선 방향

- nonlocal 변수를 피하고 dfs가 해당 서브트리의 카운트를 반환하도록 변경해 함수형 스타일로 구현 가능
- 입력 크기가 커질 경우를 대비해 메모이제이션으로 (index, current_sum) 상태를 캐시해 중복 계산을 줄일 수 있음
- 비트마스크나 itertools.product를 사용해 반복적으로 모든 부호 조합을 생성하는 더 간결한 구현 가능

## 📝 회고

- 재귀 기반 완전탐색에서 종료 조건을 리프 노드에서 처리하는 패턴 숙지 필요
- 상태 전달 방식(전역/클로저 vs 반환값) 선택에 따른 가독성·테스트 용이성 차이 인지 필요
- 문제 크기에 따라 완전탐색의 지수 시간 복잡도를 다른 기법(동적 계획법·메모이제이션)으로 개선할 수 있음

---

*풀이 코드를 기반으로 자동 생성한 초안입니다.*
