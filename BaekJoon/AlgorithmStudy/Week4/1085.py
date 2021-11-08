x,y,w,h = map(int, input().split())

result = []

result.append(abs(x-0))
result.append(abs(y-0))
result.append(abs(w-x))
result.append(abs(h-y))

print(min(result))