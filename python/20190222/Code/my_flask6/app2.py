"""
Flask-cache
web应用缓存的前提:
  1. 某个请求耗时(涉及到后台操作比较多)
  2. 长时间内(5min-30min)页面保持不变
"""
from flask import Flask
from flask_cache import Cache
app = Flask(__name__)
# 默认存在python解释器内存中，生产中一般参与缓存服务器如：redis，memcached
cache = Cache(app, config={
  'CACHE_TYPE': 'simple'
})

@app.route('/')
@cache.cached(timeout=5)
def index():
  print('view index')
  return 'index'

@app.route('/posts')
def get_posts():
  return ', '.join(get_posts())

@cache.cached(timeout=5, key_prefix='get_posts')
def get_posts():
  print('methods: get_posts')
  return ['a', 'b', 'c', 'd']

@app.route('/comments/<int:num>')
def get_comments(num):
  return ', '.join(get_comments(num))

@cache.memoize(timeout=5)
# @cache.cached(timeout=5, key_prefix='get_comments')
def get_comments(num):
  print('methods: get_comments')
  return [str(i) for i in range(num)]

def clear_cache():
  cache.delete('get_posts')  # 删除指定缓存
  cache.delete_many('get_posts', 'index')  # 删除多个缓存
  cache.delete_memoized('get_comments')
  cache.clear()  # 清除所有缓存

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)