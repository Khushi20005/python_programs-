# Write a python program to reverse a string.
str1=input("enter a string ")
print("The",str1,"in reverse order is : ")
length=len(str1)
for a in range(-1,(-length-1),-1):
    print(str1[a])

# FOR BETTER OUTPUT PURPOSE.
str1=input("enter a string:")
length=len(str1)
i=0
for a in range(-1,(-length-1),-1):
    print(str1[i],"\t",str1[a])
    i+=1