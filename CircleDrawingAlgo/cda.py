class CDA:
    def __init__(self):
        self.x, self.y, self.r = list(map(int, input().split()))[:3]
        self.octant_1 = []
        self.octant_2 = []
        self.octant_3 = []
        self.octant_4 = []
        self.octant_5 = []
        self.octant_6 = []
        self.octant_7 = []
        self.octant_8 = []
        self.cda()
        # print(self.x, self.y, self.r)
    
    
    
    def cda(self):
        x = 0
        y = self.r
        p = 3 - 2*self.r
        self.octant_one.append([x+self.x, y+self.y])
        # print(p)
        
        while True:
            x += 1
            if p < 0: p = p+4*x+6
            else:
                y -= 1
                p = p+4*(x-y)+10
                
            
            if x>y: break
            # print(p)
            self.octant_one.append([x+self.x, y+self.y])
        
        for d in self.octant_one:
            print(d)
                
            

def main():
    ob = CDA()
    

if __name__=="__main__":
    main()