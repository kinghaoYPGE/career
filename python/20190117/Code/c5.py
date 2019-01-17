"""
匿名函数(lambda表达式)
"""
a = lambda x: print(x) # 计算因子
a(1)
list_a = [1, 2, 3, 4, 5]
r = map(lambda x: x**2, list_a)
print(list(r))
from functools import reduce
r = reduce(lambda x, y: x+y, list_a)
print(r)

# 三元运算符
# 真 if 条件判断 else 假
list_b = '1223471034710345610340'
r = [(0 if int(i)<=2 else 9) for i in list_b]
print(r)

# 便函数
r = int('1000101001', base=2)
# print(bin(r))
print(r)
def int2(x, base=2):
    return int(x, base)
r = int2('1010000101001')
print(r)
from functools import partial
int2 = partial(int, base=16)
r = int2('324192470AEB')
print(r)