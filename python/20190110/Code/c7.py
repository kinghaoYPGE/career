# 类的定制

# __str__和__repr__用法
class Student(object):
    def __init__(self, name):
        self.name = name
        # self.score = 98
    def __str__(self):
        return 'Student(name:%s)' % self.name

    # def __repr__(self):
        # return 'Student(name:%s)' % self.name
    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    def __call__(self):
        print('Student name is %s' % self.name)
    
# s = Student('zhangsan')
# print(s)

# __getitem__用法
class BookCollection(object):
    def __init__(self):
        self.book_list = ['a', 'b', 'c', 'd']

    def __getitem__(self, n):
        return self.book_list[n]

    
# book_collection = BookCollection()
# r = book_collection.book_list[1]
# r = book_collection[2]
# print(r)

# __getattr__用法
s = Student('zhangsan')
print(s.score)
#__call__用法
s()
print(callable(s))
print(callable([1, 2, 3]))