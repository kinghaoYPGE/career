age = input('please enter your age:' )
age = int(age)
if age >= 18:
    print('your age is %d' % age)
    print('you are a adult')
elif age >=6:
    print('teenager')
else:
    print('kid')
