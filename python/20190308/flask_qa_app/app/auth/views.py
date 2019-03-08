from flask import Blueprint, request, jsonify, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app.models import User
from sqlalchemy import or_

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        _form = request.form
        User(
            username=_form.get('username'),
            email=_form.get('email'),
            password=_form.get('password')
        ).save()
        return jsonify(status='success', info='用户创建成功')
    except ValueError as e:
        return jsonify(status='error', info=str(e))
    except Exception as e:
        print(e)
        raise


@auth_bp.route('/login', methods=['POST'])
def login():
    _form = request.form
    try:
        # select * from t_user where username=? or email=?
        user_instance = User.query.filter(or_(User.username==_form.get('username'),
                                              User.email==_form.get('email'))).first()
        if user_instance and user_instance.verify_password(_form.get('password')):
            login_user(user_instance.seen())  # 登陆成功后更新访问时间
        else:
            flash(message='用户名/邮件或密码不一致', category='error')
    except Exception as e:
        print(e)
        raise
    return redirect(url_for('qa.index'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('qa.index'))

