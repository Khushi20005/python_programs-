#Create a function count_vowels(s) that takes a string s as input and returns the
#number of vowels in the string.
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels(input("enter any string")))