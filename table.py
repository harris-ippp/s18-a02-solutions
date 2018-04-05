import mortgage

# read inputs from command line
price = float(input('Home price: '))
down_min = float(input('Minimum down payment: '))
down_max = float(input('Maximum down payment: '))
rate = float(input('Interest rate: '))
term = float(input('Loan term (years): '))

rate = rate / 100 / 12

# use range function to enumerate down payments
for down in range(int(down_min), int(down_max), 1000):
    loan = price - down
    payment = mortgage.calculate_payment(loan, rate, term*12)

    print(down, round(payment, 2))
