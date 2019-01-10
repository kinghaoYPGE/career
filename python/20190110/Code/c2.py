class Student(object):
   pass

s = Student()
s.name = 'zhangsan'
print(s.name)
# 函数就是一个可调用对象
# 匿名函数(lambda表达式)
# def print_hello():
#     print('hello')
s.hello= lambda : print('hello')
s.hello()
print(s.__dict__)

# 对象动态添加方法，只对当前实列有效
def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# s2 = Student()
# s2.set_age(30)

# 类动态添加实例方法，对所有实例有效
Student.set_age = set_age
s.set_age(20)
s2 = Student()
s2.set_age(18)
print(s.age, ',', s2.age)



