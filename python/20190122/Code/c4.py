"""
序列化: 把对象从内存中转换成可存储的对象并写入到磁盘
反序列化: 把序列化后的对象读取到内存
"""
import pickle
dict_a = {'name': 'zhangsan', 'age': 20, 'score': 99.9}
# print(id(dict_a))
# dict_a_bytes = pickle.dumps(dict_a)

# 序列化
# with open('c4_dump.txt', 'wb') as f:
    # pickle.dump(dict_a, f)

# 反序列化
# with open('c4_dump.txt', 'rb') as f:
    # dict_b = pickle.load(f)
    # print(id(dict_b))
    # print(dict_b)

# pickle序列化操作只适用于python

# XML
# JSON-标准数据传输规范, 序列化标准格式, 轻量级, 传输速度快
# json是一个轻量级数据交换格式
# 微服务架构, 每个功能都是一个服务(REST服务), 用户管理系统是Java开发的, 订单系统是python开发的
# JSON 序列化和反序列化
# JSON字符串-不同服务数据交换的载体 如: {"name": "zhangsan", "age": 20, "score": 99.9}
# JSON-Python的映射关系:
# {}-dict, []-list, string-str, 12.1-float/int
import json
json_str = json.dumps(dict_a)

print(json_str)

dict_c = json.loads(json_str)
print(dict_c)
# json序列化
with open('c4_json.txt', 'w', encoding='utf-8') as f:
    json.dump(dict_a, f)

# json反序列化
with open('c4_json.txt', 'r', encoding='utf-8') as f:
    dict_c = json.load(f)

