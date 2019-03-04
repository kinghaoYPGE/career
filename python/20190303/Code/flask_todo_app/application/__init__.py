from config import load_config
from flask import Flask
from application.extensions import db, login_manager, admin
from flask_admin.contrib.mongoengine import ModelView
from application.controllers import all_bp
from application.models import User, Role


def create_app(mode):
    """工厂方法用于生成flask app"""
    config = load_config(mode)
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprint(app)
    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()

    admin.init_app(app)
    # admin.add_view(ModelView(User))
    admin.add_view(ModelView(Role))


def register_blueprint(app):
    for bp in all_bp:
        app.register_blueprint(bp)

