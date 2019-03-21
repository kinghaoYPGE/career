from flask import Flask
import time
import threading
app = Flask(__name__)

@app.route('/')
def index():
  print('index %s' % threading.currentThread())
  time.sleep(5)
  return 'index'

@app.route('/hello/<name>')
def hello(name):
  print('hello %s' % threading.currentThread())
  time.sleep(5)
  return 'hello %s' % name

if __name__ == '__main__':
  print('main %s' % threading.currentThread())
  app.run()