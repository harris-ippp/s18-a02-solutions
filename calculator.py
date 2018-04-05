import mortgage

# read inputs from terminal
price = float(input('Home price: '))
down = float(input('Down payment: '))
rate = float(input('Interest rate: '))
term = float(input('Loan term (years): '))

loan = price - down # calculate loan amount
rate = rate / 100 / 12 # calculate monthly rate as a decimal
payment = mortgage.calculate_payment(loan, rate, term*12)

print(round(payment, 2))
