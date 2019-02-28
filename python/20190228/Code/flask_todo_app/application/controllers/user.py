from flask import Blueprint

user_bp = Blueprint('users', __name__, url_prefix='')

@user_bp.route('/users')
def index():
  return 'index'
