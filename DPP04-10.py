#Write a Python function monthly_payment(principal, rate, years) that
#calculates the monthly mortgage payment for a given principal loan amount, annual
#interest rate, and loan term in years. Use the formula
def monthly_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    num_payments = years * 12
    if rate == 0:
        return principal / num_payments
    
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    return payment
principal = 300000 
rate = 3.5         
years = 30       

print(monthly_payment(principal, rate, years))