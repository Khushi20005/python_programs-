#Write a Python function factorial(n) that calculates and returns the factorial of a
#number n using recursion.
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
x=int(input("enter any number:"))
y=factorial(x)
print("factorial of ",x,"is",y)