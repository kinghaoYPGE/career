class Student():
    # name = 'zhangsan'
    # age = 0
    student_count = 0

    # 构造方法--实例化时候就调用
    def __init__(self, name, age=18, score=60):
        # print('this is __init__')
        self.__class__.student_count += 1
        # print(self.__class__.student_count)
        self.name = name
        self.age = age 
        self.score = score

    # 实例方法
    def learn(self):
        self.score = 89.9
        print('%s is learning, his age is %s and score is %s' % (self.name, self.age, self.score))
        print('learning...')

    # 类方法
    @classmethod
    def print_student_count(cls):
        print(cls.student_count)

    # 静态方法
    @staticmethod
    def print_version(obj):
        print('this is student version 1.0')
        print(obj)
        print(Student.student_count)
        
if __name__ == '__main__':
    # Student.name = 'lisi'
    # print(Student.name)
    # stu.name = 'abc'
    # print(Student.name)
    # print(stu.name)
    # print(stu.name, stu.age, stu.score)
    # stu1 = Student('lisi', 20, 98.0)
    # print(stu1.name, stu1.age, stu1.score)
    # stu2 = Student('xiaoming')
    # print(stu2.name)
    # 动态添加对象(实例)成员
    # stu.score = 99.9 
    # stu.name = 'abc'
    # stu.learn()
    # print(stu.score)
    stu = Student('zhangsan', 19, 89.8)
    # print('student:' ,stu.__dict__, '\n', 'Student:', Student.__dict__)
    # print(dir(stu))
    stu2 = Student('zhangsan', 19, 89.8)
    stu3 = Student('zhangsan', 19, 89.8)
    # stu.name = 'lisi'
    # stu.learn()
    # stu.print_student_count()
    # Student.print_student_count()
    Student.print_version(Student)
    stu.print_version(stu)
