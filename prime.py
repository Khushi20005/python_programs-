num=int(input("enter number to check prime or not"))
temp=False
if num==1 or num==0:
    print("not prime")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            temp=True
            break
    if temp:
            print("not prime")
    else:
            print("prime")