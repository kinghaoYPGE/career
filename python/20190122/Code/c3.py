"""
文件和目录操作: 增删改查(CRUD)
"""
import os
print(os.name)  # 当前操作系统
# os 模块的函数是和操作系统相关的
# print(os.uname())  # windows没有这个方法
print(os.environ.get('PATH'))  # 拿到操作系统的环境变量

# 操作文件和目录
print(os.path.abspath('.'))  # 查看当前目录的绝对路径
testdir = os.path.join('C:\develop\Inspiration\career\python', 'test_dir')
# os.mkdir(testdir)  # 创建一个目录
# os.rmdir(testdir)  # 删除一个目录
# 得到文件路径和文件名
r = os.path.split(r'C:\develop\Inspiration\career\python\20190122\file\test.txt')
# 得到文件扩展名
r = os.path.splitext(r'C:\develop\Inspiration\career\python\20190122\file\test.txt')
print(r)
# 对文件重命名
# os.rename('c2.py', 'c2.txt')
# 删除文件
# os.remove('test.txt')
# 复制文件
# os模块没有提供复制文件的方法
# os补充模块 shutil
# from shutil import copyfile
# copyfile('c1.py', 'c1_1.py')
# 列出指定目录下所有的文件和目录
dirs = os.listdir(r'C:\develop\Inspiration\career\python')
# 列出指定目录下的所有目录
r = [i for i in dirs if os.path.isdir(i)]
code_dir = r'C:\develop\Inspiration\career\python\20190122\Code'
code_dirs = os.listdir(code_dir)
# 列出指定目录下所有的py文件
r = [i for i in code_dirs if os.path.isfile(os.path.join(code_dir, i)) \
and os.path.splitext(i)[1] == '.py'] 
print(r)
