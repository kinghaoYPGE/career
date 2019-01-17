"""
python常用高阶函数
map, reduce, filter, sorted
"""
# map reduce 是一个算法模型--hadoop(map/reduce:映射，规约)，并行计算
# map 映射
list_a = [1, 2, 3, 4, 5]
def my_square(x):
    return x**2
r = map(my_square, list_a)
print(list(r))

# reduce
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# 从序列头计算到尾
from functools import reduce
def minus(x, y):
    return x - y
r = reduce(minus, list_a)
# [1, 2, 3, 4, 5] -->12345
# def my_fn(x, y):
#     return x*10 + y
# r = reduce(my_fn, list_a)
# def char2num(s):
#     list_a = list(range(10))
#     list_b = list(map(chr, list(range(48, 58))))
#     return dict(zip(list_b, list_a))[s]
# r = reduce(my_fn, map(char2num, '123579'))

def str2int(s):
    def my_fn(x, y):
        return x*10 + y
    def char2num(s):
        list_a = list(range(10))
        list_b = list(map(chr, list(range(48, 58))))
        return dict(zip(list_b, list_a))[s]
    return reduce(my_fn, map(char2num, s))

r = str2int('134314234')
print(r)




