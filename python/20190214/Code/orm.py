"""
orm简易实现
1 将python对象的属性和数据库表的字段建立映射关系
2 对对象进行增删改查操作，那么也应自动生成对应的sql语句，并执行
"""
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'int')

class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar')

class ModelMetaclass(type):
    def __new__(self, name, bases, attrs):
        if name == 'Model':
            return type.__new__(self, name, bases, attrs)
        print(3*'*', '%s' % name)
        # 建立映射关系
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = 't_' + name.lower()
        return type.__new__(self, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('model has no attr %s' % key)
    
    def __setattr__(self, key, value):
        self[key] = value

    # 新增记录(生成对应的insert语句)
    def save(self):
        # insert into table_name(?, ?, ?) values(?, ?, ?)
        fields = [] # 表的字段
        params = [] # 表字段对应的?
        args = []  # 表字段具体的值
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = r'insert into %s(%s) values(%s)' \
        % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL is: %s' % sql)
        print('args is: %s' % str(args))

