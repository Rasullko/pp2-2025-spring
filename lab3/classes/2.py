class Shape:
    def area(self):
        return 0
    
class Square:
    def __init__(self, len):
        self.len = len
    
    def area(self):
        return self.len ** 2
    
s = Square(int(input()))
print(s.area())