# RECTANGLE

class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        
    @classmethod
    def property(cls, leng, bread):
        return cls(leng, bread)
    
    def area(self):
        return self.length * self.breadth
    
    def is_square(self):
        return True if self.length == self.breadth else False
    
    
rec = Rectangle.property(4, 4)
print(rec.area())
print(rec.is_square())