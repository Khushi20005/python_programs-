#Write a Python function add_two_numbers(a, b) that takes two numbers as input
#and returns their sum.
def add_two_numbers(a,b):
    c=a+b
    return c
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=add_two_numbers(x,y)
print("the sum of given number",z)
