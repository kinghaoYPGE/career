"""
C = (F - 32) / 1.8
"""
F = 0
print('Fahrenheit', 'Celsisus')
while F <= 250:
    C = (F - 32) / 1.8
    print('{:5d} {:12.2f}'.format(F, C))
    F = F + 25
else:
    print('transfer finished')
