def func1():
    print('this is func1')

def func2():
    """
    把函数作为一个返回值
    """
    return func1

def func_wrapper(fo, name):
    """
    把函数作为一个参数
    """
    print("this is %s's name" % name)
    fo()
    
