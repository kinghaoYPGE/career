"""
flask-mongoengine用法
flask-login用法:https://www.cnblogs.com/minsons/p/8045916.html
登陆只是粗粒度权限管理
细粒度权限管理实现:
[读取记录，新建记录，更新记录，删除记录]
RBAC: role-based access control用于给user分配角色，然后给角色分配权限(CRUD)
权限: 二进制来表示 如:
R:0001
C:0010
U:0100
D:1000
..
RCUD:1111
"""
from flask import Flask, jsonify, abort, request
from flask_mongoengine import MongoEngine
from flask_login import login_user, logout_user, login_required, current_user
from flask_login.login_manager import LoginManager
import json
from datetime import datetime
from enum import Enum
from functools import wraps
login_manager = LoginManager()
db = MongoEngine()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
  'db': 'flask_db',
  'host': '127.0.0.1',
  'port': 27017
  # 'username':...
  # 'password':...
}
app.config['SECRET_KEY'] = '123'
db.init_app(app)
login_manager.init_app(app)

class Permission():
  READ = 0x01
  CREATE = 0x02
  UPDATE = 0x04
  DELETE = 0x08
  DEFAULT = READ

class Role(db.Document):
  name = db.StringField()
  permission = db.IntField()

if Role.objects.count() <= 0:
  READ_ROLE = Role('READER', Permission.READ).save()
  CREATE_ROLE = Role('CREATOR', Permission.CREATE).save()
  UPDATE_ROLE = Role('UPDATER', Permission.UPDATE).save()
  DELETE_ROLE = Role('DELETER', Permission.DELETE).save()
  DEFAULT_ROLE = Role('DEFAULT', Permission.DEFAULT).save()
else:
  READ_ROLE = Role.objects(permission=Permission.READ).first()
  CREATE_ROLE = Role.objects(permission=Permission.CREATE).first()
  UPDATE_ROLE = Role.objects(permission=Permission.UPDATE).first()
  DELETE_ROLE = Role.objects(permission=Permission.DELETE).first()
  DEFAULT_ROLE = Role.objects(permission=Permission.DEFAULT).first()

class User(db.Document):
  meta = {
    'collection': 'user',
    'strict': False,
    'ordering': ['-create_time']
  }
  name = db.StringField(required=True)
  pwd = db.StringField(required=True)
  create_time = db.DateTimeField(default=datetime.now)
  role = db.ReferenceField('Role', default=DELETE_ROLE)

  # 是否激活
  def is_active(self):
    return True

  # 是否认证
  def is_authenticated(self):
    return True
  
  def is_anonymous(self):
    return False

  def get_id(self):
    return str(self.id)

class Article(db.Document):
  meta = {
    'collection': 'article',
    'strict': False,
    'ordering': ['-create_time']
  }
  title = db.StringField()
  content = db.StringField()
  create_time = db.DateTimeField(default=datetime.now)
  
  def to_json(self):
    return {
      'title': self.title,
      'content': self.content,
      'create_time': self.create_time
    }

@app.route('/blog/api/users', methods=['POST'])
def user_register():
  """创建新的用户"""
  # 产过来的数据应该也是json类型
  if not request.json or not 'username' in request.json:
    abort(400)
  user = User(name=request.json['username'], pwd=request.json['password'], role=DEFAULT_ROLE)
  user.save()
  return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
  username, password = request.json['username'], request.json['password']
  user = User.objects(name=username, pwd=password).first()
  if user:
    # 执行登陆
    login_user(user)
    return jsonify(user)
  else:
    return jsonify({'result': 'Invalid username or password'}), 401

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return jsonify({'status':'success'})
@login_manager.user_loader
def load_user(user_id):
  return User.objects(id=user_id).first()

@app.route('/blog/api/articles', methods=['GET'])
def get_articles():
  """获取所有文章"""
  # return json.dumps(articles)
  articles = Article.objects().all()  #.order_by('-create_time')
  return jsonify(articles)

@app.route('/blog/api/articles/page/<int:page>', methods=['GET'])
# def get_articles_by_page(page):
#   page = page-1
#   limit = 1
#   """获取所有文章"""
#   # return json.dumps(articles)
#   articles = Article.objects().all().skip(page).limit(limit)
#   return jsonify(articles)
def get_articles_by_page(page):
  # page = page-1
  limit = 1
  """获取所有文章"""
  # return json.dumps(articles)
  articles = Article.objects.paginate(page=page, per_page=limit)
  return jsonify(articles.items)

@app.route('/blog/api/articles/<article_id>', methods=['GET'])
def get_article(article_id):
  """获取某个文章"""
  article = Article.objects(id=article_id).first()
  if not article:
    abort(404)
  return jsonify(article.to_json())

def permission_control(permission):
  def decorator(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
      if not current_user.is_authenticated:
        abort(401)
      user_permission = current_user.role.permission
      if user_permission & permission == permission:
        return func(*args, **kwargs)
      else:
        abort(403)
    return decorated_func
  return decorator

@app.route('/blog/api/articles', methods=['POST'])
@permission_control(Permission.CREATE)
def create_article():
  """创建新的文章"""
  # 产过来的数据应该也是json类型
  if not request.json or not 'title' in request.json:
    abort(400)
  article = Article(title=request.json['title'], content=request.json['content'])
  article.save()
  print(article)
  return jsonify(article), 201

@app.route('/blog/api/articles/<article_id>', methods=['PUT'])
def update_article(article_id):
  article = Article.objects(id=article_id).first()
  # 判断文章是否存在
  if not article:
    abort(404)
  # 判断修改参数是否合法
  if not request.json:
    abort(400)
  # 进行修改
  article.update(title=request.json['title'], content=request.json['content'])
  return jsonify(article)

@app.route('/blog/api/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
  article = Article.objects(id=article_id).first()
  # 判断文章是否存在
  if not article:
    abort(404)
  article.delete()
  return jsonify({'result': True})

@app.errorhandler(404)
def page_not_found(error):
  return jsonify({'error': 'Not found'}), 404
@app.errorhandler(400)
def bad_request(error):
  return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(401)
def bad_request(error):
  return jsonify({'error': 'Authenticated failed'}), 401

@app.errorhandler(403)
def bad_request(error):
  return jsonify({'error': 'access forbidden'}), 403

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8089, debug=True)
