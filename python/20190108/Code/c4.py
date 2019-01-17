# type
r = type(999)
print(r)
r = type('abc')
print(r)
r = type(None)
print(r)
r = type(abs)
print(r)
from c3 import Person, Student
p = Person('lisi', 'M')
r = type(p)
print(r)
print(type(123)==type('abc'))

import types
print(type(abs)==types.BuiltinFunctionType)

# isinstance
stu = Student('zhangsan', 'F')
r = type(stu)==type(p)
print(r)
# 判断类型，优先使用isinstance
r = isinstance(stu, (list, Person))
print(r)

# dir
# print(dir())
# print(dir(Person))
# print(dir(Student))
# print(dir(123))
# print(dir('abc'))
# print(dir(p))
# print(dir(stu))

r = len('abc')
print(r)
r = 'abc'.__len__()
print(r)
r = len(stu)
print(r)
r = stu.__len__()
print(r)

