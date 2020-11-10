class Square:
    def __init__(self, side=1):
        self.side = side
    
    def setSide(self):
        if self.side < 0:
            self.side = 0
        else:
            print(self.side * self.side)

x = float(input("Side: "))           
square = Square(x)
square.setSide()
        
        
