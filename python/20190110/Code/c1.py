# 动态添加类或对象属性

class Student(object):
    name = 'Student'
    # def __init__(self, name):
    #     self.name = name
        
s = Student()
# s.score = 90
# print(s.score)

print(s.name)
print(Student.name)
s.name = 'zhangsan'
print(s.name)
print(Student.name)

del s.name
print(s.name)
Student.stu_count = 10
print(Student.stu_count)
print(s.stu_count)

