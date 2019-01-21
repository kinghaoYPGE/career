"""
记录错误
"""
# 记录日志
import logging

def f1(s):
    return 10 / int(s)
def f2(s):
    return f1(s) ** 2
def main():
    try:
        f2('0')
    except Exception as e:
        # 记录错误
        logging.exception(e)

# main()
# print('End')

# 自定义错误类型
class MyError(ValueError):
    pass

def func(s):
    n = int(s)
    if n == 0:
        # 手动抛出错误
        raise MyError('invalid value %s' % s)
    return 10 / n

def func2():
    try:
        func('0')
    except ValueError as e:
        # 捕捉错误的目的就是记录一下，为了后续跟踪
        # 当前函数不知道怎么处理这个错误
        print('ValueError: ', e)
        # 进行错误类型转换
        raise

# print(func('1'))
# print('End')
func2()
print('End')
