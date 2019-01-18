"""
生成器: 是一个函数
"""
from collections import Iterable, Iterator
list_a = [i for i in range(0, 10001)]
# print(list_a)

def my_genrator(max):
    n = 0
    while n <= max:
        n += 1
        yield n

g = my_genrator(10000)
r = isinstance(g, Iterable)
print(r)
r = isinstance(g, Iterator)
print(r)
print(type(g))
print(g)
for i in range(0, 10):
    print(next(g))

# 生成器表达式
g2 = (i for i in range(0, 10001))
print(g2)
print(type(g2))
print(next(g2))


