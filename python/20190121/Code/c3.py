"""
代码调式:
1. print语句-有效的，但是不推荐
2. 断言: assert
3. 日志: logging
4. 日志级别:
    4.1 info
    4.2 debug
    4.3 warning
    4.4 error
5. pdb:python自带的调式器
"""
def func(s):
    n = int(s)
    # 断言如果为False会抛出AssertionError
    # python -O 执行可以忽略assert断言相当于pass语句
    assert n != 0, 'n is zero'
    return 10 / n

import logging
# 设置日志级别为info
logging.basicConfig(level=logging.INFO)
def func2(s):
    n = int(s)
    logging.info('n: %d' % n)
    return 10 / n

def main():
    r = func2('0')
    print(r)
main()