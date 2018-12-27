import getpass
username = input('please enter your username: ')
password = getpass.getpass('please enter your password: ')
user_level = {'root':'admin', 'zhangsan':'VIP1', 'lisi':'VIP2', 'others':''}

# if 'root' != username:
if username not in user_level:
    print('invalid username!')
elif 'root' != password:
    print('invalid password!')
else:
    print('login successfully!')
    if 'root' == username:
        print('welcome admin!')
    elif 'zhangsan' == username:
        print('welcome VIP1')
    elif 'lisi' == username:
        print('welcome VIP2')
    else:
        print('you are so poor')



