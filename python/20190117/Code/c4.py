"""
返回函数
"""
def my_add(*args):
    result = 0
    for n in args:
        result += n
    return result


def lazy_add(*args):
    def my_add():
        result = 0
        for n in args:
            result += n
        return result
    return my_add

# r = my_add(1, 2, 3, 4, 5)
fn = lazy_add(1, 2, 3, 4, 5)
fn2 = lazy_add(1, 2, 3, 4, 5)
r = fn == fn2
# print(r)

# 闭包(Closure)
def my_count():
    def f(j):
        def g():
            return j**2
        return g
    fns = []
    for i in range(1, 4):
        fns.append(f(i))
    return fns

f1, f2, f3 = my_count()
r = f1()
r2 = f2()
r3 = f3()
# print(r, r2, r3)
# print(f1.__closure__[0].cell_contents)

# 定位蚂蚁在沙漠的位置如: 0->1->3->5-?
# 非闭包方式
origin = 0
def go(step):
    global origin
    newpos = origin+step
    origin = newpos
    return newpos

# 闭包方式
# 闭包的环境变量会常存内存
# 代码里不宜过多定义全局变量
def factory(pos=0):
    def go(step):
        nonlocal pos
        newpos = pos + step
        pos = newpos
        return pos
    return go

ant_go = factory()
print(ant_go(1))
print(ant_go(2))
print(ant_go(2))
cat_go = factory()
print('*'*6)
print(cat_go(2))
print(cat_go(3))
print(cat_go(-5))


