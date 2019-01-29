# contextlib: 让实现了上下文object 可以使用with语句，减少代码
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('exit')

    def query(self):
        print('query by %s' % self.name)

from contextlib import contextmanager
class MyQuery(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('my query by %s' % self.name)

    def close(self):
        print('close')

@contextmanager
def create_query(name):
    print('enter')
    q = MyQuery(name)
    yield q
    print('exit')

with Query('zhangsan') as q:
    q.query()

with create_query('zhangsan') as q:
    q.query()

# 自定义标签
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)

with tag('h1'):
    print('hello')
    print('python')


# closing: 如果一个对象没有实现上下文，可以通过closing方法
from contextlib import closing
with closing(MyQuery('lisi')) as q:
    q.query()
