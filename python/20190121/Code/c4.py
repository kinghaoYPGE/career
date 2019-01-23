"""
断点调式
1. pdb: python -m pdb sample.py(进入pdb模式)
    1.1 常用命令: l(查看当前代码),n(执行下一步),p 变量名(查看当前变量)
    1.2 缺点: 一般只适合少量代码
    1.3 优化: 加断点-pdb.set_trace()
        1.3.1 命令补充: c(执行下一个断点)

2. IDE断点调式功能

"""
import pdb

s = '0'
n = int(s)
s1 = '2'
n1 = int(s1)
s2 = '4'
n2 = int(s2)
# pdb.set_trace()  # 设置断点
s3 = '5'
n3 = int(s3)
# pdb.set_trace()  # 设置断点
print(10 / n)
print(10 / n2)
print(10 / n3)
