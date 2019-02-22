# 导入模块
import sqlite3
from flask import Flask, request, session, redirect, url_for, \
render_template, flash, g, abort
from contextlib import closing

# 创建应用
app = Flask(__name__)
# 配置
app.config.from_pyfile('config.py')

# 连接数据库
def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

# 初始化表
def init_db():
  # 封装成上下文对象，不需要手动关闭db
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql') as f:
      db.cursor().executescript(f.read().decode())
    db.commit()

@app.before_request
def before_request():
  # g对象只能保存一次请求的信息
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  g.db.close()

# 业务处理
# 页面倒序显示所有条目
@app.route('/')
def show_entries():
  cur = g.db.execute('select title, text from entries order by id desc')
  entries = [{'title':row[0], 'text':row[1]} for row in cur.fetchall()]
  return render_template('entries.html', entries=entries)

# 添加新的条目
@app.route('/add', methods=['POST'])
def add_entry():
  if not session.get('user'):
    return redirect(url_for('login'))
  g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
  g.db.commit()
  flash('Add Successfully!')
  return redirect(url_for('show_entries'))

# 登陆
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
      error = 'Invalid username or password'
    else:
      session['user'] = request.form['username']
      return render_template('entries.html')
  return render_template('login.html', error=error)

# 注销
@app.route('/logout')
def logout():
  session.pop('user', None)
  flash('Logout successfully!')
  return redirect(url_for('show_entries'))


@app.errorhandler(401)
def auth(error):
  return render_template('401.html', error=error)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089)
