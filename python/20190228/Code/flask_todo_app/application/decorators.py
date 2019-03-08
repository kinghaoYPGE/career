from flask import abort
from functools import wraps
import application.models as Models


def permission_control(permission):
  """
  自定义装饰器用于角色权限管理
  """
  def decorator(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
      from flask_login import current_user
      # if role is normal then permission is 7
      user_permission = Models.Role.objects(name=current_user.role).first()
      if (user_permission.permission & permission) == permission:
        return func(*args, **kwargs)
      else:
        abort(403)
    return decorated_func
  return decorator