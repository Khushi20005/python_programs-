#WAP to print grade.
marks=int (input("enter marks"))
if marks==100:  
    print("A+")
elif(marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks<=90):
    print("B+")
elif(marks>=70 and marks<=80):
    print("B")
elif(marks>=60 and marks<=70):
    print("C")
elif(marks>=30 and marks<=60):
    print("you are pass")
else:
    print("you are fail")
