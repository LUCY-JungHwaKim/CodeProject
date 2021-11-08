from collections import Counter

rectangle_x = []
rectangle_y = []

for _ in range(3):
    x,y = map(int, input().split())

    rectangle_x.append(x)
    rectangle_y.append(y)

print(str(Counter(rectangle_x).most_common()[-1][0]) + " " + str(Counter(rectangle_y).most_common()[-1][0]))
