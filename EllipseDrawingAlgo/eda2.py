class MEA:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.pixels = []
    
    def mea(self):
        x = 0
        y = self.b
        
        sa = self.a * self.a
        sb = self.b * self.b
        dx = 2*x*sb
        dy = 2*y*sa
        p = sb - sa*self.b + sa/4
        # print("==> ", p)
        
        # print(dx, dy)
        while dx < dy:
            # Plot(x + x0, y + y0)    Quadrant 1
			# Plot(x - x0, y + y0)    Quadrant 2
			# Plot(x + x0, y - y0)    Quadrant 3
			# Plot(x - x0, y - y0)    Quadrant 4
            self.pixels.append([x, y])
            # print("Hi")
            x += 1
            dx = dx + 2 * sb
            f = True if p>=0 else False
            p = p + 2 * sb*x + sb
            
            
            if f:
                y -= 1
                p = p - sa*y
                dy = dy - 2 * sa
            
            # print("==> ", p)
        
        self.pixels.append([x, y])
        
        q = sb*(x + 1/2)*(x + 1/2) + sa*(y - 1)*(y - 1) - sa*sb
        
        while y > 0:
            # Plot(x + x0, y + y0)    Quadrant 1
			# Plot(x - x0, y + y0)    Quadrant 2
			# Plot(x + x0, y - y0)    Quadrant 3
			# Plot(x - x0, y - y0)    Quadrant 4
            y -= 1
            
            if q > 0:
                dy = dy - 2 * sa
                q = q + sa - dy
            else:
                x += 1
                dx = dx + 2 * sb
                dy = dy - 2 * sa
                q = q + dx - dy + sa
            
            self.pixels.append([x, y])


obj = MEA(0, 0, 8, 6)
obj.mea()
print(obj.pixels)
                
        
            