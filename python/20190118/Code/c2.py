"""
带参数的装饰器
"""
"""
def log(f):
    @wraps(f)
    def wrapper(*args, **kwards):
        print('call: '+f.__name__)
        return f(*args, **kwards)
    return wrapper
"""
from functools import wraps
def log(content):
    def log_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwards):
            print(content+': call-->%s' % content)
            return f(*args, **kwards)
        return wrapper
    return log_decorator


@log('DEBUG')
def f1():
    return 'this is f1'

@log('ERROR')
def f2():
    return 'this is f2'

r = f1()
print(r)
r = f2()
print(r)
print(f1.__name__)
