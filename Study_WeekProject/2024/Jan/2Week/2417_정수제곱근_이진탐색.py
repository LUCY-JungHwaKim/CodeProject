n = int(input())

l,r = 0, n

while True:
    mid = (l+r)//2

    if r < l:
        break

    if mid ** 2 >= n:
        r = mid -1
    else:
        l = mid + 1

print(r+1)