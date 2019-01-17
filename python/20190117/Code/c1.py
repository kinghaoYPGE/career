"""
函数式编程: 抽象程度很高的编程范式
    允许把函数本身作为参数或者返回值
存粹的函数式编程语言是没有变量的(Lisp)
    任意一个函数,输入时确定的,输出就是确定的,没有副作用
"""
# 高阶函数
# 变量可以指向一个函数
my_abs = abs
r = my_abs(-10)
# print(r)
# 函数名就是变量名
def my_fn():
    pass
# print(my_fn)
# 函数作为另一个函数的参数
def add(x, y, fn):
    return fn(x) + fn(y)

r = add(-5, -9, abs)
print(r)