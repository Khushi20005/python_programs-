#Write a program to check wheather a number is prime or not.
a=int(input("enter the value of a:"))
for i in range(2, a-1):
    if a%i !=0:
        print(a,"number is prime number")
        break
    else:
        print(a,"the number is not a prime number")
    break
