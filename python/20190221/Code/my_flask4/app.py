from flask import Flask, jsonify, abort, request
import json
app = Flask(__name__)

# 定义articles
articles = [
  {
    'id': 1,
    'title': 'python',
    'content': 'python is good'
  },
  {
    'id': 2,
    'title': 'flask',
    'content': 'flask is good'
  }
]

@app.route('/blog/api/articles', methods=['GET'])
def get_articles():
  """获取所有文章"""
  # return json.dumps(articles)
  return jsonify({'articles': articles})

@app.route('/blog/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
  """获取某个文章"""
  article = list(filter(lambda a: a['id'] == article_id, articles))
  if len(article) == 0:
    abort(404)
  return jsonify({'article': article[0]})

@app.route('/blog/api/articles', methods=['POST'])
def create_article():
  """创建新的文章"""
  # 产过来的数据应该也是json类型
  if not request.json or not 'title' in request.json:
    abort(400)
  article = {
    'id': articles[-1]['id'] + 1,
    'title': request.json['title'],
    'content': request.json.get('content', '')
  }
  articles.append(article)
  return jsonify({'article':article}), 201

@app.route('/blog/api/articles/<int:article_id>', methods=['PUT'])
def update_article(article_id):
  article = list(filter(lambda a: a['id'] == article_id, articles))
  # 判断文章是否存在
  if len(article) == 0:
    abort(404)
  # 判断修改参数是否合法
  if not request.json:
    abort(400)
  # 进行修改
  article[0]['title'] = request.json.get('title', article[0]['title'])
  article[0]['content'] = request.json.get('content', article[0]['content'])
  return jsonify({'article': article[0]})

@app.route('/blog/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
  article = list(filter(lambda a: a['id'] == article_id, articles))
  # 判断文章是否存在
  if len(article) == 0:
    abort(404)
  articles.remove(article[0])
  return jsonify({'result': True})

@app.errorhandler(404)
def page_not_found(error):
  return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def page_not_found(error):
  return jsonify({'error': 'Bad request'}), 400
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8089, debug=True)