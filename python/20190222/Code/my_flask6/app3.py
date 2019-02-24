"""
Flask-HTTPAuth:
web应用有时为了避免API非法访问，需要进行HTTP认证
1. 密码: 默认
2. 令牌(token): 推荐
"""
from flask import Flask, jsonify, g, url_for, redirect
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask'
auth = HTTPTokenAuth(scheme='Token')

# 实例化签名对象, 有效期10分钟
serializer = Serializer(app.config['SECRET_KEY'], expires_in=600)

# tokens = {
#   'token-1': 'zhangsan',
#   'token-2': 'lisi'
# }

users = ['zhangsan', 'lisi']
# 生成token
for user in users:
  token = serializer.dumps({'username': user})
  print('User: %s Token: %s' % (user, token)) 

# 回调函数
# @auth.verify_password
# def verify_password(username, password):
#   if username == 'admin' and password == 'admin':
#     g.user = username
#     return True
#   return False
@auth.verify_token
def verify_token(token):
  g.user = None
  try:
    data = serializer.loads(token)
  except:
    return False
  if 'username' in data:
    g.user = data['username']
    return True
  return False

@app.route('/')
@auth.login_required
def index():
  # return '<form method=post action='+url_for('add')+'><input type=submit value=submit></form>'
  return 'Hello %s' % g.current_user

@app.route('/add', methods=['POST'])
@auth.login_required
def add():
  return redirect(url_for('index'))

@auth.error_handler
def unauthorized():
  return jsonify({'error': 'Unauthorized Access'}), 401

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)
