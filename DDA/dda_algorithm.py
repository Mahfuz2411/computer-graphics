import math as mt

class DDA:
    def __init__(self, start: list, end: list) -> None:
        self.start: list = start
        self.end: list = end
        self.points: list = []
    
    def findPoints(self) -> list[list[int, int]]:
        dx = self.end[0] - self.start[0]
        dy = self.end[1] - self.start[1]
        
        m: int = dy/dx if dx else 0
        
        step: int = dx if abs(m) <= 1 else dy
        
        xinc = dx/step if step else 0
        yinc = dy/step if step else 1
        
        self.points.append(self.start)
        
        x: int
        y: int
        
        x, y = self.start
        while 1:
            x += xinc
            y += yinc
            
            if x>self.end[0] or y>self.end[1]: break
            self.points.append([round(x), round(y)])
        
        return self.points


def main():
    start = list(map(int, input("Start: ").split()))[:2]
    end = list(map(int, input("End: ").split()))[:2]
    # ob = DDA(start, end)
    # ob.findPoints()
    # print(ob.points)
    print(DDA(start, end).findPoints())
    

if __name__ == "__main__":
    main()