#Write a Python function circle_area(radius) that takes the radius of a circle and
#returns the area of the circle. (Use the formula: Area = π × radius², assume π = 3.1416).
"""import math
def circle_area(radius):
    a=math.pi*radius*radius
    return a
x=int(input("enter the radius of circle"))
y=circle_area(x)
print("area of circle is:",y)'"""

#OR

def circle_area(radius):
    a=3.1416*radius*radius
    return a
x=int(input("enter the radius of circle"))
y=circle_area(x)
print("area of circle is:",y)