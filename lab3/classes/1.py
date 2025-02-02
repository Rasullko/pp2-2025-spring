class Str:
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())
    
s = Str()
s.getString()
s.printString()
