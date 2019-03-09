#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, request, current_app, redirect, url_for, jsonify, flash
from sqlalchemy import or_
from flask_login import login_user, logout_user, login_required
from app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        _form = request.form
        User(
            email=_form.get('email'),
            username=_form.get('name'),
            password=_form.get('password')
        ).save()
        return jsonify(status="success", info=u"创建成功")
    except ValueError as e:
        # flash(message=str(e), category='error')
        return jsonify(status="error", info=str(e))
    except Exception as e:
        # current_app.logger.error(e)
        # flash(message='用户已存在', category='error')
        raise


@auth_bp.route('/login', methods=['POST'])
def login():
    _form = request.form
    try:
        user_instance = User.query.filter(or_(User.username==_form.get('name'),
                                              User.email==_form.get('email'))).first()
        if user_instance and user_instance.verify_password(_form.get('password')):
            login_user(user_instance.seen())  # 登陆并更新用户访问时间
        else:
            flash(message='用户名/邮件或密码错误', category='error')
    except Exception as e:
        current_app.logger.error(e)
    return redirect(url_for('qa.index'))


@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('qa.index'))
