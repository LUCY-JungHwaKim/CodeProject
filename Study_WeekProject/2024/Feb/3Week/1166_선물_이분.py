n, l, w, h = map(int, input().split())

left = 0
right = max(l,w,h)

for _ in range(10000):
    mid = (left + right) / 2

    # if mid > l or mid > w or mid > h : ## 값의 범위가 넘어가면, xx
    #     right = mid - 1

    total = (l // mid) * (w // mid) * (h // mid)

    if total >= n:
        left = mid
    else:
        right = mid

print("%.10f" %(right))

