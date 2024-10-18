# Print numbers in a list until a negative number is encountered using a while loop.
list1=[2,5,7,10,25,-6,18,20,22]
index=0
while index < len(list1):
    if list1[index]<0:
        break
    print(list1[index])
    index += 1
