from app import User
from app import db
def query():
  users = User.query.all()  # 查询所有记录
  print(users)
  user = User.query.filter_by(username='zhangsan').first()  # 按名字查询
  # print(str(User.query.filter_by(username='zhangsan')))
  user = User.query.filter(User.username=='zhangsan').first()  # 按名字查询
  # print(str(User.query.filter(User.username=='zhangsan')))
  print(user)

  # 分页方法
  users = User.query.limit(4).offset(2).all()
  print(users)

def update():
  user = User.query.filter_by(username='zhangsan').first()
  print('before update:', user.email)
  user.email = 'zs@zhangsan.com'
  print('after update:', user.email)
  db.session.add(user)
  db.session.commit()

def delete():
  user = User.query.filter_by(username='zhangsan').first()
  db.session.delete(user)
  db.session.commit()

if __name__ == '__main__':
  # query()  # 查询数据
  # update()  # 更新数据
  delete()  # 删除数据