ary = [5,7,9,0,3,1,6,2,4,8]

def quick_srt(ary, strt, end):
    if strt >= end: ## ,원소가 1개인 경우 종료
        return

    pv = strt # 제일 첫번재 원소
    left = strt +1 # 왼쪽 시작 지점 인덱스
    right = end # 오른쪽 시작 지점 인덱스

    while left <= right:

        # 피봇보다 큰 데이터 찾을 때까지 반복
        while left <= end and ary[left] <= ary[pv]:
            left += 1

        # 피봇보다 작은 데이터 찾을 때까지 반복
        while right > strt and ary[right] >= ary[pv]:
            right -= 1

        # 만약 엇갈린다면 left의 인덱스가 right 인덱스보다 크다면
        if left > right:
            ## right (작은 값)이랑 피봇 값 위치 변경
            ary[right], ary[pv] = ary[pv], ary[right]
        else: ## 그렇지 않다면 작은값, 큰값 교환
            ary[left], ary[right] = ary[right], ary[left]

    ## 피봇 옮긴 후 양쪽 리스트 재정렬 시행

    quick_srt(ary, strt, right-1)
    quick_srt(ary, right+1, end)

quick_srt(ary, 0, len(ary)-1)

print(ary)