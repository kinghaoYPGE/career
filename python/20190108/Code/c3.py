class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__salary = 1000
    
class Student(Person):
    def __init__(self, name, gender, score=99):
        # Person.__init__(self, name, gender)
        # Person().__init__(name, gender)
        # super(Student, self).__init__(name, gender)
        super().__init__(name, gender)
        self.score = score

    def __len__(self):
        return 100
if __name__ == '__main__':
    p = Person('zhangsan', 'M')
    print(p.__dict__)
    stu = Student('lisi', 'M')
    print(stu.__dict__)
