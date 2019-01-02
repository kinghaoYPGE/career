"""
python变量作用域
1 局部变量不会覆盖全局变量
2 局部变量不会被外部引用
3 局部没有会去找上一级
4 global会使局部变量变成全局变量
"""
# a = 20
def fun1():
    a = -10
    def fun2():
        # a = 10  # 局部变量
        print(a)
    return fun2

#fun1()()
#print(a)

def change():
    global a
    a = 100
    print(a)
    #a = 100
change()
print(a)


