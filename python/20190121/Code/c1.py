"""
一、程序错误:
1. 程序编写的时候有问题-bug
2. 用户输入脏数据-通过检查校验来对用户输入进行处理
3. 程序运行过程中无法预测的，比如：网络问题, 磁盘问题等-异常
4. 业务问题
程序中所有的错误都需要进行处理
二、程序调式:
跟踪程序的执行，查看相应变量的值
三、程序测试:
测试人员：程序上生产(production)之前，会通过多个测试环境(test, uat, stg)
开发人员：单元测试(开发环境)

"""
# 获取python自带异常错误类
# import re
# list_a = dir(__builtins__)
# list_b = [i for i in list_a if re.match(r'.*(Error|Exception)$', i)]
# list_c = list(filter(lambda x: re.match(r'.*(Error|Exception)', x),list_a))
# print(list_c)

# try 语句
"""try:
    print('try...')
    r = 10 / int('2')
    print('resutl:', r)
except ValueError as e:
    print('value except:', e)
except ZeroDivisionError as e:
    print('zero except:', e)
# else:
    # print('no error..')
finally:
    # 可以做一些资源关闭
    print('finally')
print('End')"""

# python错误类都是BaseException的子类
# print(isinstance(ValueError(), BaseException))
"""
错误栈:
Traceback (most recent call last):
  File "c:/develop/Inspiration/career/python/20190121/Code/c1.py", line 47, in <module>
    main()
  File "c:/develop/Inspiration/career/python/20190121/Code/c1.py", line 46, in main
    f2('0')
  File "c:/develop/Inspiration/career/python/20190121/Code/c1.py", line 44, in f2
    return f1(s) ** 2
  File "c:/develop/Inspiration/career/python/20190121/Code/c1.py", line 42, in f1
    return 10 / int(s)
ZeroDivisionError: division by zero"""
def f1(s):
    return 10 / int(s)
def f2(s):
    return f1(s) ** 2
def main():
    f2('0')    
main()
print('End')



