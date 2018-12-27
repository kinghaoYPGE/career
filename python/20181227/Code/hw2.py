import sys
cmd_args = sys.argv

number = int(cmd_args[1])
target = cmd_args[2]

if '2' == target:
    print('%s transfer to %s with bin' % (number, bin(number)))
elif '8' == target:
    print('%s transfer to %s with oct' % (number, oct(number)))
elif '16' == target:
    print('%s transfer to %s with hex' % (number, hex(number)))
else:
    print('please input correct target!')


