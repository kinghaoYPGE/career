"""
itertools: 对操作可迭代对象的补充
"""
import itertools
from collections import Iterable, Iterator
# 无限迭代器
iter_count = itertools.count(2)
print(type(iter_count))
print(isinstance(iter_count, Iterable))
print(isinstance(iter_count, Iterator))
print(next(iter_count))
print(next(iter_count))
# for n in iter_count:
    # if n > 100:
        # break
    # print(n)
# cycle
cs = itertools.cycle('python')
# for i in cs:
    # print(i)

# repeat
rp = itertools.repeat('A', 10)
for n in rp:
    print(n)

# takewhile 条件
r = itertools.takewhile(lambda x: x <= 100, iter_count)
# print(list(r))
# for i in r:
    # print(i)

# chain()
# iter_a = '123'
# iter_b = 'abc'
# for i in itertools.chain(iter_a, iter_b):
    # print(i)

# groupby: 分组
group_by = itertools.groupby('AAABBBBCCCDDDD')
for k, group in group_by:
    print(k, list(group))
