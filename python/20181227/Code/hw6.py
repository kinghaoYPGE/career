"""
****
***
**
*
"""
row = int(input('Enter number of rows: '))
row_2 = row
row_3 = row
while row >= 0:
    x = '*' * row
    print(x)
    row -= 1

i = 1
while i <= row_2:
    print('*' * i)
    i += 1

n = row_3
while n  >= 0:
    x = '*' * n
    y = ' ' * (row_3 - n)
    print(y + x)
    n -= 1
