#Write a python program to count total number of digits in a number.
number=(input("enter the number:"))
digit_count=0
for char in number:
    if char.isdigit():
        digit_count +=1
print("total number of digits:",digit_count)