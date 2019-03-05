from .auth import auth_bp
from .todo import todo_bp
from .utils import utils_bp
from application.api import api_bp

all_bp = [
  auth_bp,
  todo_bp,
  utils_bp,
  api_bp
]