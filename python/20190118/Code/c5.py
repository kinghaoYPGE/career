"""
迭代器, 可迭代对象
迭代器需要实现两个内置方法
__iter__
__next__
"""
from collections import Iterable, Iterator

# list_a = [1, 2, 3]
# r = isinstance(list_a, Iterator)
# print(r)
# next(list_a)

class BookCollection(object):
    def __init__(self):
        self.cursor = 0
        self.data = ['java', 'python', 'c#', 'javascript']
    def __iter__(self):
        return self
    def __next__(self):
        if self.cursor > len(self.data)-1:
            raise StopIteration()
        else:
            self.cursor += 1
            return self.data[self.cursor-1] 

bookCollection = BookCollection()
import copy
bookCollection_copy = copy.copy(bookCollection)
r = isinstance(bookCollection, Iterable)
print(r)
r = isinstance(bookCollection, Iterator)
print(r)
# while True:
    # r = next(bookCollection)
    # print(r)
    
# for book in bookCollection:
    # print(book)
print(next(bookCollection))
print(next(bookCollection))
print(next(bookCollection))
print(next(bookCollection))
print(next(bookCollection))
