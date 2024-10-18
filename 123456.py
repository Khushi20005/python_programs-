# Write to check largest number when the user enter the three number.
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if(a>b and a>c):
    print("a is the largest number")
elif(b>a and b>c):
    print("b is the largest number")
else:
    print("c is the largest number")