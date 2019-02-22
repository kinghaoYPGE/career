"""
会话:session
登陆
"""
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

# 保证当前会话安全
app.secret_key = 'python'

@app.route('/')
def index(name=None):
  # 如果是登陆状态，显示用户名
  if 'user' in session:
    return '<a href='+url_for('logout')+'>Logout</a> Login as %s' % session.get('user')
  return 'Please <a href='+url_for('login')+'>Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['user'] = request.form['username']
    return redirect(url_for('index'))
  return '''
          <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="Login"></p>
          </form>
         '''

@app.route('/logout')
def logout():
  # 从session中移除user
  session.pop('user', None)
  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)