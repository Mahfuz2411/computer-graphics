x1, y1 = list(map(int, input("First point: ").split()))[:2]
x2, y2 = list(map(int, input("Second point: ").split()))[:2]

dx = abs(x1 - x2)
dy = abs(y1 - y2)
m = dy/dx
steps = dx if m<=1 else dy

xinc = round(dx/steps, 2)
yinc = round(dy/steps, 2)

data = []
data.append([x1, y1])

x, y = x1, y1
for _ in range(steps):
    x += xinc
    y += yinc
    x = round(x, 2)
    y = round(y, 2)
    data.append([round(x), round(y)])

for arr in data:
    print(arr)