"""
重定向、错误和响应对象
"""
from flask import Flask, redirect, url_for, abort, render_template, make_response

app = Flask(__name__)

@app.route('/')
def hello(name=None):
  return redirect(url_for('login'))

@app.route('/login')
def login():
  # abort(404)
  try:  
    1/0
  except Exception as e:
    app.logger.error(e)
    abort(500)
  return 'please login'

@app.errorhandler(404)
def page_not_found(error):
  # 响应对象
  # 返回元组: (response, [status], headers[消息头列表或者字典])
  return render_template('404.html', error=error), 404

@app.errorhandler(500)
def server_error(error):
  # return render_template('500.html', error=error), 500
  resp = make_response(render_template('500.html', error=error), 500)
  resp.headers['Exception'] = error
  return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)