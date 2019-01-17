def func(a, word='hello', *para, **kwords):
    print(type(para))
    print(para)
    for i in para:
        print(i)

def func1(**kwords):
    print(type(kwords))
    print(kwords)
    for k,v in kwords.items():
        print(k,':', v)


# 任意函数(装饰器会用到)
def func3(*params, **kwords):
    pass
        
    
          
