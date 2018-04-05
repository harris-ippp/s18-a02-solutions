import mortgage

# read inputs from terminal
price = float(input('Home price: '))
rate = float(input('Interest rate: '))
term = float(input('Loan term (years): '))
payment = float(input('Desired monthly payment: '))

rate = rate / 100 / 12 # calculate monthly rate as decimal

# initial interval for search is [0, price]
a = 0.0
b = price

while True:
    c = (a + b)/2
    Fc = mortgage.calculate_payment(price - c, rate, term*12)

    if (abs(fc - payment) < 1):
        break
    elif fc < payment:
        b = c
    else:
        a = c
