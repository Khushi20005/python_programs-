#WAP to accept the cost price of a bike and display the road tax to be paid according to the following criteria
#cost price(in rupees - 15% tax )
#100000 -15%
#50000 - 10% and <=100000  10% 
# >= 50000 - 5%
cost_price=int(input("enter the price of bike"))
if(cost_price>100000):
    print("tax is 15%")
elif(cost_price>=50000 and cost_price<=100000):
    print("tax is 10%")
else:
    print("tax is 5%")