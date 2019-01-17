# 对象存在不一定就是True
# 通过__bool__和__len__方法一起决定，但__bool__优先级高
# class Student(object):
#     def __bool__(self):
#         return False 

#     def __len__(self):
#         return 1
    

# s = Student()
# print(bool(s))
# print(len(s))

# 自定义可比较对象
# python2 用的是__cmp__内置方法
# python3 用的是__lt__和__gt__方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __gt__(self, s):
        if self.score > s.score:
            return 1
        elif self.score < s.score:
            return -1
        else:
            # 如果分数相同，按照姓名去排序
            return 0

s1 = Student('zhangsan', 99)
s2 = Student('lisi', 89)

print(dir(s1))
# r = sorted([s1, s2])
r = s1 > s2
print(r)