# Write a program to check if a string is a palindrone(read the same forwards and backwards).
"""a=input(" Enter a string to check palindrome : ")
if a==a[::-1]:
    print("IT IS PALINDROME")
else:
    print("IT IS NOT PALINRDOME")"""


def ispalindrome(string):
    if(string==string[::-1]):
       return "the string is a palindrome"
    else:
        return "this is not palindrome"
string=input("enter string:")
print(ispalindrome(string))