from .auth import auth_bp
from .todo import index_bp, todo_bp
from application.utils import utils_bp
from application.api import api_bp

all_bp = [
  index_bp,
  auth_bp,
  todo_bp,
  utils_bp,
  api_bp
]
