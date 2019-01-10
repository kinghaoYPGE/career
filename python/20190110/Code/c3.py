# 对象内置变量__slots__: 控制对象动态添加属性
class Student(object):
    __slots__ = ['name', 'age']
    
class ManStudent(Student):
    __slots__ = ['score']
    
stu = Student()
stu.name = 'lisi'
print(stu.name)
# stu.score = 20
# print(stu.score)
Student.name = 'Student'
print(Student.name)
Student.score = 99
print(Student.score) 
man_stu = ManStudent()
man_stu.score = 90
print(man_stu.score)
man_stu.name = 'lisi'
print(man_stu.name)