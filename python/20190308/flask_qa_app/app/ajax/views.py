from flask import Blueprint, request, jsonify
from app.models import User

ajax_bp = Blueprint('ajax', __name__, url_prefix='/ajax')


@ajax_bp.route('/user/username_check', methods=['POST'])
def username_exist_or_not():
    username = request.form.get('username')
    user = User.query.filter(User.username==username).first_or_404()
    if user:
        return jsonify(status='error', info='用户名已注册')


@ajax_bp.route('/user/email_check', methods=['POST'])
def email_exist_or_not():
    email = request.form.get('email')
    user = User.query.filter(User.email==email).first_or_404()
    if user:
        return jsonify(status='error', info='邮箱已注册')

