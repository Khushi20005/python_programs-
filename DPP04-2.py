#Define a function find_maximum(a, b) that accepts two numbers and returns the
#larger number.
def find_maximum(a,b):
    if a>b:
        return a
    else:
        return b
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=find_maximum(x,y)
print("the largest number:",z)