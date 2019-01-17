# from c1 import Student
# stu = Student('grace')
# print(stu.__dict__)
# print(Student.student_count)
# print(stu.learn())
class Student():
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def __print_score(self):
        print('%s: %s' %(self.name, self.__score)) # 私有变量

    def get_score(self):
        return self.__score

    def print_score(self):
        self.__print_score()
    
# stu = Student('xiaolan', 89.9)
# print(stu.name, stu.__score)
