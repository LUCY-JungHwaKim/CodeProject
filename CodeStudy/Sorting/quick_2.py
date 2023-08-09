ary = [5,7,9,0,3,1,6,2,4,8]

## 조금더 직관적인 코드
def quick_srt(ary):
    if len(ary) <=1 :## 리스트 데이터의 개수가 1개 이하면 종료
        return ary

    pv = ary[0] # 첫번째 요소 피봇 설정
    tail = ary[1:] # 피봇을 제외한 나머지를 꼬리로 설정

    left_side = [x for x in tail if x <= pv] # 피봇보다 작은 데이터를 모두 왼쪽으로
    right_side = [x for x in tail if x > pv] # 피봇보다 큰 데이터를 오른쪽으로

    return quick_srt(left_side) + [pv] + quick_srt(right_side)
    ## 왼쪽, 피봇, 오른쪽 을 합침
    ## 왼쪽은 왼쪽끼리 다시 퀵정렬, 오른쪽은 오른쪽만 퀵정렬
    ## 계속 리스트를 더하고 더하면 정렬된 데이터가 반환됨

print(quick_srt(ary))
