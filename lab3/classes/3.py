class Shape:
    def area(self):
        return 0

class Rectangle:
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    
    def area(self):
        return self.len * self.wid

a,b=map(int,input().split())
rec = Rectangle(a,b)
print(rec.area()) 