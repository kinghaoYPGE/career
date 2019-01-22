"""
IO编程
"""
# file-like Object(python鸭子特性)
# 只要实现了read方法的对象都可以使用open函数打开

# 读取二进制文件
# with open(r'C:\develop\Inspiration\career\python\20190122\img\07105030_080Q.jpg', 'r') as f:
# with open(r'C:\develop\Inspiration\career\python\20190122\file\test.txt', \
# 'r', encoding='utf-8', errors='ignore') as f:
#     print(f.read())


# 写文件
with open(r'C:\develop\Inspiration\career\python\20190122\file\test2.txt', 'w', encoding='utf-8') as f:
    f.write('你好')
with open(r'C:\develop\Inspiration\career\python\20190122\file\test2.txt', encoding='utf-8') as f:
    print(f.read())



