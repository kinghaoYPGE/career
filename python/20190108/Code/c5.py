# getattr, hasattr, setattr
from c3 import Student, Person
p = Person('lisi', 'M')
stu = Student('zhangsan', 'F')
r = hasattr(p, 'score')
print(r)
if r:
    print(p.name)
else:
    pass

# 动态设置属性
setattr(stu, 'age', 19)
stu.age = 19
r = hasattr(stu, 'weight')
if r:
    print(getattr(stu, 'age'))
    print(stu.age)
else:
    print(getattr(stu, 'weight', 90))
    # stu.weight

