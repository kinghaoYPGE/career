"""
自定义装饰器用于角色权限管理
"""
from flask import abort
from functools import wraps
import application.models as Models

def permission_control(permission):
  def decorator(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
      from flask_login import current_user
      user_permission = Models.Role.objects(name=current_user.role).first()
      if (user_permission & permission) == permission:
        return func(*args, **kwargs)
      else:
        abort(403)
    return decorated_func
  return decorator