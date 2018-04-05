# function to calculate payment
# given loan value, monthly interest rate, and number of months
def calculate_payment(loan, rate, periods):
    return rate*loan/(1-(1+rate)**(-periods))
