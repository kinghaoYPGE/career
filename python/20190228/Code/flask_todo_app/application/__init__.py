from config import load_config
from flask import Flask
from application.controllers import all_bp

def create_app(mode):
  """工厂方法用于生成flask app"""

  config = load_config(mode)
  app = Flask(__name__)
  app.config.from_object(config)
  register_blueprint(app)
  return app

def register_blueprint(app):
  for bp in all_bp:
    app.register_blueprint(bp)