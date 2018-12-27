# value = amount + (rate * amount)
# period

amount = float(input('Enter amount: '))
rate = float(input('Enter Interest rate: '))
period = int(input('Enter period: '))
value = 0
year = 1

while year <= period:
    value = amount + (rate * amount)
    print('Year {:2d} Value {:.2f}'.format(year, value))
    amount = value
    year += 1



