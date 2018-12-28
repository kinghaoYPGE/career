"""
--> 1x1 = 1
    1x2 = 2..
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d x %d = %d' % (j, i, i*j), end='\t')
    print()


