"""
python orm框架sqlalchemy的使用
"""
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # 定义表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(30))
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(30))
    # 建立一个user_id 外键
    user_id= Column(String(20), ForeignKey('user.id'))


# 连接数据库
engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/mysql_test")
# 如果表不存在，自动创建表
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
user = User(id='123', name='zhangsan')
# 新增一条数据
session.add(user)
session.commit()

# 查询表的数据
user = session.query(User).filter(User.id=='123').one()
print(user.id, user.name)
print(type(user.books))
print(','.join([book.name for book in user.books]))
session.close()