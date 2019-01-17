# 多重继承(MixIn), 组合功能使用

# 角色树
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

# 技能树
class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    pass

class FootballMixin(SkillMixin):
    pass

# 增强对象
class BasketballStudent(Student, BasketballMixin):
    pass
class FootballTeacher(Teacher, FootballMixin):
    pass

# 实列化会打篮球的学生
b_stu = BasketballStudent()

# 实例化会踢足球的老师
f_ter = FootballTeacher()

