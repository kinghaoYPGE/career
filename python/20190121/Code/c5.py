"""
测试
1. 开发测试(开发环境)
  1.1 单元测试: 对一个模块，一个函数，一个类等进行正确性检验的测试
2. 业务测试(测试环境)
"""
# 针对abs函数有如下测试用例：
# 1. 输入正数-->和输入相同
# 2. 输入负数--> 和输入相反
# 3. 输入0 --> 还是0
# 4. 输入非数值 --> 抛出TypeError

"""
编写一个字典类，要求如下:
d = Dict(a=1, b=2, c=4)
d['a']
d.a
d.a = '1'
"""
class Dict(dict):
    """
    this is my dict
    example:
    >>> d1 = Dict()
    >>> d1['x'] = 1
    >>> d1.x
    1
    """
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            print(e)
            raise AttributeError('no attribute: %s' % key)
        

    def __setattr__(self, key, value):
        self[key] = value

def abs(n):
    """
    this is abs function
    example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n>=0 else (-n)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(abs.__doc__)



    



