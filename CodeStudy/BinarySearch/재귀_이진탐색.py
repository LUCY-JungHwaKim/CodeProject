## 재귀 함수로 작성하는 이진탐색

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
    

n, target = map(int, input().split())

ary = list(map(int, input().split()))

result = binary_search(ary, target, 0, n-1)

if result == None:
    print("해당 원소 없음")
else:
    print(result+1) ##인덱스 값 말고 가시적인 위치 출력
