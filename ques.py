#write python function to find maximum of three numbers.
def maximum(a,b,c):
    if (a>b and a>c):
        print("largest number",a)
    elif (b>a and b>c):
        print("largest number",b)
    else:
        print("largest number",c)
    return(maximum)
print(maximum(12,56,10))