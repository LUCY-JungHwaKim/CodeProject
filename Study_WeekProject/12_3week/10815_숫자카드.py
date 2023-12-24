import sys
input = sys.stdin.readline

n = int(input())
n_ary = sorted(list(map(int, input().split())))

m = int(input())
m_ary = list(map(int, input().split()))

## 시간 초과 안나게 코드 작성 잘 해야함, 이분 탐색

for m in m_ary:

    start = 0
    end = n - 1
    chk = False
    while start <= end:
        mid = (start + end) // 2

        if n_ary[mid] == m:
            chk = True
            break
        elif n_ary[mid] > m: # 왼쪽 탐색
            end = mid - 1
        else: # 오른쪽 탐색
            start = mid + 1

    print(1 if chk else 0, end=' ')
