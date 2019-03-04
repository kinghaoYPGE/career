from flask_mongoengine import MongoEngine
from flask_login import LoginManager

db = MongoEngine()
login_manager = LoginManager()
