#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length = int(input())
width = int(input())
a = Shape()
b = Rectangle(length, width)
print(a.area())
print(b.area())