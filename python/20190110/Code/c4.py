class Student(object):

    # def __init__(self):
        # self.__score = 99
        # self.score = self.get_score()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, (int, float)):
            raise ValueError('Invalid data')
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('Invalid Score!')

stu = Student()
# stu.set_score(60)
# score = stu.get_score()
# print(score)
# stu.set_score('adfa')
# stu.set_score(999)
# stu.set_score(-99)
stu.score = 60
print(stu.score)
stu.score = 99
print(stu.score)
stu.score = -100

        