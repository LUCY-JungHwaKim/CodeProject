n, findm = list(map(int, input().split()))
ary = list(map(int, input().split()))

sum_chk = 0
s = []
rsltary = []
## dfs 재귀 사용법
def dfs(arr, lst, k):
    global sum_chk
    if lst and sum(lst) == findm:
        sum_chk += 1

    for i in range(k, n):
        lst.append(arr[i])
        dfs(arr, lst, i+1) ## 이렇게 하다보면 크기가 큰 부분 수열부터 작은 부분ㄴ수열까지 오게 됨
        #print(lst)
        lst.pop()

dfs(ary, [], 0)
print(sum_chk)
## 너무어렵다    
##백트래킹사용법
##https://www.youtube.com/watch?v=4EAg1Pmk3bw
## 코드참고 : https://seongonion.tistory.com/98
# def subset_sum(idx, sub_sum):
#     global cnt
#
#     if idx >= n:
#         return
#
#     sub_sum += arr[idx]
#
#     if sub_sum == s:
#         cnt += 1
#
#     # 현재 arr[idx]를 선택한 경우의 가지
#     subset_sum(idx + 1, sub_sum)
#
#     # 현재 arr[idx]를 선택하지 않은 경우의 가지
#     subset_sum(idx + 1, sub_sum - arr[idx])
#
#
# subset_sum(0, 0)
#
# def dfs(ary, m):
#     global sum_chk
#     #print(ary, m)
#     if len(s) == m: ## 합 구하기
#         #print(' '.join(map(str, s)))
#         s_copy = s[:] ## s가 계속해서 변하기 때문에 s의 복사본을 추가해야 함
#         s_copy.sort()
#         if s_copy not in rsltary: ## 현재꺼가 없으면 넣어주기
#             rsltary.append(s_copy)
#             if (sum(s) == findm):
#                 sum_chk += 1
#         return
#
#     for i in range(n):
#         if ary[i] not in s:
#             s.append(ary[i])
#             dfs(ary, m)
#             s.pop()
#
#
# for i in range(n):
#     dfs(ary, i+1)
#
# print(sum_chk)

# rsltary.append(s) 구문이 예상대로 동작하지 않는 이유는 s 리스트가 함수 내에서 계속 변경되기 때문입니다. 파이썬에서 리스트는 가변 객체(mutable object)이므로, 리스트를 다른 리스트에 추가할 때 실제 객체의 참조가 추가됩니다. 이는 s가 함수 내에서 변경될 때마다 rsltary에 추가된 모든 s 참조들도 동일하게 변경된다는 것을 의미합니다.
#
# 이 문제를 해결하기 위해서는 s의 현재 상태의 복사본을 rsltary에 추가해야 합니다. 이를 위해 list(s) 또는 s[:]를 사용하여 s의 복사본을 만들 수 있습니다.
#
# 또한, s.sort() 구문이 s를 정렬하기 때문에, 이 정렬된 s가 rsltary에 저장됩니다. 만약 원본 순서대로 결과를 저장하고 싶다면, s를 정렬하기 전에 복사해야 합니다.
## 라고 챗지ㅣ피티가 잡아줌..