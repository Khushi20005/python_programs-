#Print a pattern of stars using nested for loop.
a=int(input("enter the no."))
for i in range(0,a):
    for j in range(0,i+1):
        print("*",end=" ")
    print()