from application.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash

__all__ = ['User', 'Permission', 'Role']


class Permission(object):
    """
    RBAC(Role Based access control)
    """
    READ = 0x01  # 0001
    CREATE = 0x02  # 0010
    UPDATE = 0x04  # 0100
    DELETE = 0x08  # 1000


class Role(db.Document):
    name = db.StringField(unique=True)
    permission = db.IntField()


class User(db.Document):
    username = db.StringField(required=True)
    email = db.StringField(required=True)
    password_hash = db.StringField()
    todolists = db.ListField()
    role = db.StringField(default='NORMAL')  # NORMAL = 7

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        self.save()  # 更新

    @property
    def id(self):
        return str(self._id)

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'role': self.role
        }

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

