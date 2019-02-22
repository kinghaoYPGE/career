from flask import Flask, render_template
from book import book
from movie import movie

# app = Flask(__name__)

# app工厂方法
def create_app(config_filename):
  app = Flask(__name__)
  # 基础配置
  app.config.from_pyfile(config_filename)
  # 注册蓝图
  app.register_blueprint(book.book_bp)
  app.register_blueprint(movie.movie_bp)

  # 错误处理
  handle_errors(app)
  return app

def handle_errors(app):
  @app.errorhandler(404)
  def page_not_found(error):
    return render_template('404.html'), 404

  @app.errorhandler(500)
  def page_not_found(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
  app = create_app('config/prod_config.py')
  app.run(host='0.0.0.0', port=8089, debug=True)