from c2 import Student

stu = Student('lisi', 98.9)
print(stu.name)
stu.__score = 99.99  # 对象动态添加成员
print(stu.__score)
print(stu.__dict__)
# print(Student.__dict__)
# # print(stu._Student__score)
# score = stu.get_score()
# print(score)
# stu.print_score()