from flask import Flask, url_for, render_template, reqeust, make_response
# __name__决定程序的根目录，可以定位到静态文件，模板文件的位置
app = Flask(__name__)

# 路由: 定义了一个URL到Python函数的映射关系
@app.route('/', methods=['GET', 'POST'])
# 视图函数
def index():
    # todo
    return 'Hello Flask'
# 动态路由
@app.route('/hello')
@app.route('/hello/<username>')
def hello(username=None):
    #return 'Hello %s' % username
    return render_template('hello.html', username=username)

@app.route('/id/<int:id>')
def hello2(id):
    #  print(type(id))
    return 'id: %s' % id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath
# 通过url_for动态构建url，避免url硬编码
@app.route('/url')
def test_url_for():
    return url_for('hello')

@app.route('/css/<file>')
def get_css(file):
    return url_for('static', filename=file)

# 请求对象
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # 执行登录操作
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username']
        else:
            error = 'Invalid username or password'
        # 用户请求其他参数
        # request.args.get('key', '')
    return render_template('login.html', error=error)  # 返回登录页面

# 文件上传
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file1']
        # f.filename
        from werkzeug import secure_filename
        # 得到客户端上传的文件名
        print(secure_filename(f.filename))
        f.save('/var/temp/upload/file.txt')

# cookies
@app.route('/cookies')
def cookies():
    # 得到cookie
    username = request.cookies.get('username')
    # 返回cookie到浏览器
    resp = make_response(render_templeate('home.html'))
    resp.set_cookie('username', 'zhangsan')
    return resp


if __name__ == '__main__':
    # 轮询，等待并处理请求
    # Flask内置的web服务器不适合用于生产
    app.run(host='0.0.0.0', port=8000, debug=True)
