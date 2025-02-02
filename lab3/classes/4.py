from math import sqrt

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self, x_m, y_m):
        self.x += x_m
        self.y += y_m
    
    def distance(self, x2, y2):
        return sqrt((x2-self.x)**2 + (y2-self.y)**2)
    
x,y=map(int,input().split())
points = Points(x,y)
points.show()
x_m, y_m = map(int,input().split())
points.move(x_m, y_m)
points.show()
print(points.distance(x_m, y_m))