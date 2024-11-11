"""Ques10. How do you define a method within a class?
 ○ Write a simple example of a class with a method"""

#To define a method within a class, you write a function inside the class definition. This function must include self as its first parameter, allowing the method to access and modify the instance’s attributes.

#Example:
#Here’s a simple example of a class with a method:

#python
#Copy code
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        # Method to calculate the area of the circle
        return 3.14159 * (self.radius ** 2)

# Creating an instance of Circle
my_circle = Circle(5)

# Calling the method
print(my_circle.area())  # Output: 78.53975