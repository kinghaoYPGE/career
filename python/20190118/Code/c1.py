"""
装饰器
"""
import time
from functools import wraps

# 无参装饰器
def my_func(func):
    @wraps(func)
    def wrapper(*args, **kwards):
        # 加上你新增需求代码
        print(time.time())
        return func(*args, **kwards)
    return wrapper

# 语法糖
@my_func
def f1():
    # 违背了开闭原则
    # print(time.time())
    print('this is f1')

@my_func
def f2():
    print('this is f2')

@my_func
def f3():
    print('this is f3')

@my_func
def f4(a):
    print('this is f4', a)

def f5(a, b=2):
    print('this is f5', a + b)

# def print_current_time(func):
    # print(time.time())
    # func()

# print_current_time(f1)
# print_current_time(f2)
# print_current_time(f3)

# f1 = my_func(f1)
# f1()
# f2()
# f3()
f1()
f4(2)
f5(3, b=5)
print(f1.__name__)
