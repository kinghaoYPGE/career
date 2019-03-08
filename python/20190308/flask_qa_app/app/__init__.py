from configs import config
from flask import Flask
from app.extensions import db, login_manager, migrate
from app.blueprints import all_bp


def register_extensions(app):
    """注册flask扩展"""
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    migrate.init_app(app=app, db=db)


def register_blueprints(app):
    """注册蓝图"""
    for bp in all_bp:
        app.register_blueprint(bp)


def create_app(mode):
    conf_obj = config.get(mode or 'default')
    app = Flask(__name__)
    app.config.from_object(conf_obj)
    register_extensions(app)
    register_blueprints(app)
    return app
