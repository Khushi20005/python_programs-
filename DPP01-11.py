# Find the first occurence of a number in a list using a while loop.
numbers=[1,2,3,5,3]
target=3
index=0
found=-1
while index < len(numbers):
    if numbers[index]==target:
        found=index
        break
    index +=1
    print("first occurence of",target,"is at index:",found)