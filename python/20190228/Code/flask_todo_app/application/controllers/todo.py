from flask import Blueprint

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')


@todo_bp.route('/')
def index():
    return 'index'