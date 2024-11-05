x1, y1 = list(map(int, input().split()))[:2]
x2, y2 = list(map(int, input().split()))[:2]

dx = abs(x1 - x2)
dy = abs(y1 - y2)
# print(dx, dy)
m = dy/dx
# steps = (2*dy-dx) if m<1 else (2*dx-dy)
# print("m =", m)
type = 1 if m<1 else 0
# print('type = ', type)

print("Points are: ")
print(x1, y1)

x, y = x1, y1
if type:
    pk = 2*dy-dx
    while x != x2:
        x += 1
        if pk < 0:
            pk = pk+2*dy
        else:
            pk = pk + 2*dy - 2*dx
            y += 1
        print(x, y)
        # print("pk =", pk)
else:
    pk = 2*dx-dy
    while y != y2:
        y += 1
        if pk < 0:
            pk = pk+2*dx
        else:
            pk = pk + 2*dx - 2*dy
            x += 1
        print(x, y)


print('\n\nEnd')