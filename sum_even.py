#Write a python program to calculate the sum of all even numbers starting from 1 to 100.
sum_of_all_numbers=0
for i in range(2,101,2):
    sum_of_all_numbers=sum_of_all_numbers+i
print("The sum of all even numbers starting from 1 to 100.",sum_of_all_numbers)