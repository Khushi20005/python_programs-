# Mid-Level Coding Problems
# 1. Create a Class with Methods
#  Define a class Rectangle that has methods to calculate the area and perimeter. Instantiate the class and print the results.
class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height
   def area(self):
       return self.width * self.height
   def perimeter(self):
       return 2*(self.width + self.height)
rect = Rectangle(5,10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


