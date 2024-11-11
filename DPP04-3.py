#Create a function is_positive(num) that checks if a given number is positive. The
#function should return True if the number is positive and False otherwise.
def is_positive(num):
    if num>0:
        return True
    else:
        return False
x=int(input("enter the value of x:"))
y=is_positive(x)
print(y)