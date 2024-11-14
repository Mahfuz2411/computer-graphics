class EDA:
  def __init__(self, x, y, a, b):
    self.x = x
    self.y = y
    self.a = a
    self.b = b
    self.points_1 = []
    self.points_2 = []
    self.points_3 = []
    self.points_4 = []
    
  def eda(self):
    x = 0
    y = self.b
    sa = self.a * self.a
    sb = self.b * self.b
    dx = 2 * x * sa
    dy = 2 * y * sb
    
    p = sb - sa*self.b + sa/4
    # print("==> ", p)
    
    while dx < dy:
      self.points_1.append([x+self.x, y+self.y])
      self.points_2.append([-x+self.x, y+self.y])
      self.points_3.append([-x+self.x, -y+self.y])
      self.points_4.append([x+self.x, -y+self.y])
      
      
      x += 1
      f = True if p>=0 else False
      p = p + 2*sb*x+ sb
      dx = dx + 2*sb
      
      
      # y = y - 1 if f else y
      # p = p - sa*y if f else p
      if f:
        y -= 1
        p = p - 2*sa*y
        dy = dy - 2 * sa
      # print("==> ", p)
    self.points_1.append([x+self.x, y+self.y])
    self.points_2.append([-x+self.x, y+self.y])
    self.points_3.append([-x+self.x, -y+self.y])
    self.points_4.append([x+self.x, -y+self.y])
    
    q = sb * (x+1/2)*(x+1/2) + sa*(y-1)*(y-1)-sa*sb
    
    while y>0:
      y -= 1
      if q >=0:
        q = q - 2*sa*y + sa
      else:
        x += 1
        q = q + 2*sb*x - 2*sa*y + sa
      
      self.points_1.append([x+self.x, y+self.y])
      self.points_2.append([-x+self.x, y+self.y])
      self.points_3.append([x+self.x, -y+self.y])
      self.points_4.append([-x+self.x, -y+self.y])
    
  
ob = EDA(0, 0, 8, 6)
# x, y , a, b = list(map(int, input().split()))[:4]
# ob = EDA(x, y, a, b)
ob.eda()
print("q1 = ", ob.points_1) 
print("q2 = ", ob.points_2) 
print("q3 = ", ob.points_3) 
print("q4 = ", ob.points_4) 