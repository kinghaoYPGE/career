# 符合WSGI规范的HTTP处理请求函数
def home(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = 'home'
    return [body.encode('utf-8')]

def login(env, start_reponse):
    pass
def application(env, start_response):
    method = env['REQUEST_METHOD']
    path = env['PATH_INFO']
    if method == 'GET' and path == '/':
        return home(env, start_response)
    if method = 'POST' and path == '/login':
        return login(env, start_response)
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1> hello %s web! </h1>' % (env['PATH_INFO'][1:] or 'python')
    return [body.encode('utf-8')]

# python内置WSGI服务器: wsgiref-python编写的WSGI服务器，供开发测试使用
from wsgiref.simple_server import make_server
httpd = make_server('', 8000, application)  # 创建一个服务器实例
print('Server is starting...')
httpd.serve_forever()
    
# python web 框架
# flask, django, tornado
