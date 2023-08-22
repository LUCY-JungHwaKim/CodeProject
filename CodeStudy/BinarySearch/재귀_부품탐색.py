## 재귀 함수로 작성하는 이진탐색
import sys

def binary_search(ary, target, start, end):
    if start > end:
        return None
    
    ## 중간점 지정
    mid = (start + end) // 2 ## 소수점 버리기
    
    if ary[mid] > target: ## 만약 중간점 값이 타겟보다 크면 중간점보다 한칸 당겨서 하기
        return binary_search(ary, target, start, mid-1)
    elif ary[mid] == target:
        return mid ## 원소 위치 출력
    else:
        return binary_search(ary, target, mid+1, end)
    


n = int(input())

ary = list(map(int, sys.stdin.readline().split()))  ## 입력 받는 것
ary.sort() ## 먼저 정렬 해줘야 함
m = int(input())

target = list(map(int, sys.stdin.readline().split()))

for i in range(len(target)):
    result = binary_search(ary, target[i], 0, n-1)

    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ') ##인덱스 값 말고 가시적인 위치 출력


## 연습용 코드 작성
# def binary(ary, target, start, end):
#     if start > end:
#         return None
#
#     mid = (start + end ) // 2
#
#     if ary[mid] > target:
#         binary(ary, target, start, mid - 1)
#     elif ary[mid] == target:
#         return mid ## 찾은 위치
#     else:
#         binary(ary, target, mid + 1, end)
#
# result = binary(ary, target, 0, n-1)



