"""
python中metaclass的用法
"""
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
class MyList(list, metaclass=ListMetaclass):
    pass

myList = MyList()
myList.add(1)
print(myList)

