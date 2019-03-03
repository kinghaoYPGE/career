from application.extensions import db
from werkzeug.security import check_password_hash

__all__ = ['Role', 'User', 'Permission']


class Permission(object):
    """
    权限定义: RBAC(role base access control)
    """
    READ = 0x01  # =>0001
    CREATE = 0x02  # =>0010
    UPDATE = 0x04  # =>0100
    DELETE = 0x08  # =>1000


class Role(db.Document):
    name = db.StringField(unique=True)
    permission = db.IntField()

    def __repr__(self):
        return '{}-{}'.format(self.name, self.permission)

    __str__ = __repr__

class User(db.Document):
    username = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    role = db.StringField(default='normal')
    todolists = db.ListField()

    @property
    def id(self):
        return str(self._id)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'role': self.role
        }

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


