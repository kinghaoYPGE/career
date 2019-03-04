from application.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash

__all__ = ['User']


class User(db.Document):
    username = db.StringField(required=True)
    email = db.StringField(required=True)
    password_hash = db.StringField()

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
            'email': self.email
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

