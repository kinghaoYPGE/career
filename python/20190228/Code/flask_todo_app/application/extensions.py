from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_admin import Admin

db = MongoEngine()
login_manager = LoginManager()
admin = Admin()
