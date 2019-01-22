"""
IO编程:
IO(Input/Output流)
input: 从磁盘读取文件到内存
output: 把内存计算后的数据写入到磁盘(磁盘文件, 网络等)
流: Stram
    Input Stream: 数据从磁盘流进内存
    Output Stream: 数据从内存流出到磁盘
网站:
  浏览器和服务器至少需要两个流
"""
# 文件读
# 读写文件的功能都是由操作系统提供的
# 读写文件是请求操作系统打开一个文件对象

# 读文件

try:
    f = open(r'C:\develop\Inspiration\career\python\20190121\Code\file\test.txt')
    # print(type(f))
    # print(dir(f))
    # print(f)
    # print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

# with 语句代替try语句
with open(r'C:\develop\Inspiration\career\python\20190121\Code\file\test.txt', 'r') as f:
    # 一次性读取所有内容到内存中
    # print(f.read())
    # 每次读指定字节
    # r = f.read(20)
    # print(r)
    # read方法会一次性读取文件中所有内容到内存中, readline方法可以一行一行的读取
    # readline一般用于读取配置文件
    # line = f.readline()
    # lines = f.readlines()
    # print(lines)





    

