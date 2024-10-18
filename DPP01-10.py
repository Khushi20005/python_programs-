# Calculate factorial of a number using while loop.
a=int(input("enter the number"))
fact=1
i=1
while i<=a:
    fact=fact*i
    i=i+1
    print("the factorial of",a,"=",fact)
    