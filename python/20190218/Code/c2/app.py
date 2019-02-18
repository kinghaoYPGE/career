from flask import Flask, request, render_template
app = Flask(__name__)
# 配置路由
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/')
def home():
    # 显示主页
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 判断页面请求的参数(username和密码是否是admin,如果都是说明登陆成功，否则失败)
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        return render_template('success.html', username=username)
    return render_template('form.html', message='invalid username or password')

if __name__ == '__main__':
    app.run(debug=True)
