from orm import *

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=123, name='zhangsan', email='zs@test.com', password='123')
u.save()