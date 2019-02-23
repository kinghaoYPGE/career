"""
Flask-Restful: 在Flask中更简单的提供rest服务
"""
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# @app.route('/api/articles', methods=['GET', 'POST'])
class Hello(Resource):
  def get(self):
    return {'name': 'zhangsan'}
api.add_resource(Hello, '/', '/hello')

todos = {
  1: 'reading',
  2: 'running',
  3: 'coding'
}

class Todo(Resource):
  def get(self, id):
    return {id: todos[id]}

  def put(self, id):
    todos[id] = request.form['data']
    return {id: todos[id]}
api.add_resource(Todo, '/todo/<int:id>')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)