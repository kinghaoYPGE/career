class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, s):
        print('lt')
        if self.age == s.age:
            # 如果学生年龄相同按照姓名排序
            return self.name > s.name
        return self.age < s.age
    def __le__(self, s):
        print('le')
        return self.age <= s.age
    def __eq__(self, s):
        print('eq')
        return self.age == s.age
    def __ne__(self, s):
        print('ne')
        return self.age != s.age
    def __gt__(self, s):
        print('gt')
        return self.age > s.age
    def __ge__(self, s):
        print('ge')
        return self.age >= s.age

    def __str__(self):
        return str(self.__dict__)

    __repr__ = __str__
    
s1 = Student('aisi', 19)
s2 = Student('cisi', 19)
s3 = Student('bisi', 19)
# r = s1.age > s2.age
# 按照学生的年龄进行顺序排序
# r = sorted([s1, s2])
def compare(s):
    return s.age
# r = list(sorted([s1, s2, s3], key=compare))
r = list(sorted([s1, s2, s3]))
print(r)