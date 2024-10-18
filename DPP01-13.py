# Find all the prime numbers between 1 and 50 using nested for and if.
for i in range(1,51):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print("The prime numbers between 1 and 50 is : ",i)


