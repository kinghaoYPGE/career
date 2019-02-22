"""
会话:session
登陆
"""
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

# 保证当前会话安全
app.secret_key = 'python'

@app.route('/')
def index(name=None):
  return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error = 'Invalid username or password'
    else:
      # 消息闪现
      flash('Login sucessfully!', 'info')
      flash('Warning!', 'warning')
      flash('wrong username', 'error')
      return redirect(url_for('index'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  # 从session中移除user
  session.pop('user', None)
  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)