"""
面向对象：自定义类型，而且是引用类型
类的定义
"""

class Student():
    """
    学生类型
    类变量: name, age, score
    """
    name = ''
    age = 0
    score = 0.0

    # def learn():
    #     print('i am learning python!')

    # 实例方法
    def learn(self):  # 伪关键字self
        # print(type(self))
        # print(self)
        print('i am learning python!')

student = Student()   # 实例化
# print(type(student))
print(dir(student))
# print(student)
student_name, student_age, student_score = student.name, student.age, student.score
print(student_name, student_age, student_score)
# learn_func = student.learn
# learn_func()
# print(type(student))
# print(Student)
# Student.learn()
student.learn()




    
