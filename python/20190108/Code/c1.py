class Student():
    stu_count = 0
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        self._age = 18  # 受保护的变量
    
    # 对象成员变量的setter和getter方法
    def get_score(self):
        return self.__score

    def set_score(self, score):
        # 0<=score<=100
        if 0<=score<=100:
            self.__score = score
        else:
            # 抛出一个异常
            raise ValueError('invalid score!')
        self.__score = score

stu = Student('bob', 99)
# print(stu.__dict__)
print(stu.get_score())
# stu.__score = 89
# stu.set_score(-99)
# print(stu.get_score())
print(stu._age)
# print(Student.__stu_counts
# Student.__stu_count = 10
# print(Student.__dict__)
# print(Student.__stu_count)

