"""
自定义对象转换JSON
"""
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('zhangsan', 20, 99.9)

def student2dict(s):
    return {
        'age': s.age,
        'name': s.name,
        'score': s.score
    }

json_str = json.dumps(s, default=student2dict)
print(json_str)
stu_dict = json.loads(json_str)
print(stu_dict)