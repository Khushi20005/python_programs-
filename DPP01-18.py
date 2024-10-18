# Python program to check if a given number is an armstrong number.
num=int(input("Enter three digit no. to check armstrong : "))
f=num
sum=0
while(f>0):
    a=f%10
    f=int(f/10)
    sum=sum+(a**3)
if (sum==num):
    print(num," It is an Armstrong number")
else:
    print(num,"It is not an Armstrong number")