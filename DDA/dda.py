x1, y1 = list(map(int, input("First point: ").split()))[:2]
x2, y2 = list(map(int, input("Second point: ").split()))[:2]

dx = x2 - x1
dy = y2 - y1
m = dy/dx
steps = dx if m<=1 else dy

print(dx, dy, steps)
xinc = round(abs(dx/steps), 2)
yinc = round(abs(dy/steps), 2)
if dx<0: xinc*=-1
if dy<0: yinc*=-1

data = []
data.append([x1, y1])

x, y = x1, y1
for _ in range(abs(steps)):
    x += xinc
    y += yinc
    data.append([round(x), round(y)])

for arr in data:
    print(arr)