#WAP to check an given year is leap year or not.
year=int(input("enter the year"))
a=year%100
if(a%4==0 and a%100!=0 or a%400==0):
    print("this is leap year")
else:
    print("this is not a leap year")