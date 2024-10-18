# write a program to check wheather a number entered by user divisible is by 2 or 3 (entered number should not be greater than 100).
a=int(input("enter any number"))
if(a>=100):
    print("the entered number should not be greater than 100")
elif(a%2==0 and a%3==0):
    print("the number is divisible by 2 and 3 both")
else:
    print("the number is not divisible by 2 and 3 both")
