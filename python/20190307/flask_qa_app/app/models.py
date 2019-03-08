import re
from datetime import datetime
from sqlalchemy.orm import synonym
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login_manager

EMAIL_REGEX = re.compile(r'^\S+@\S+\.\S+$')
USERNAME_REGEX = re.compile(r'^\S+$')


def check_length(attribute, length):
    """Checks the attribute's length."""
    try:
        return bool(attribute) and len(attribute) <= length
    except:
        return False


class BaseModel:
    """Base for all models, providing save, delete and from_dict methods."""

    def __commit(self):
        """Commits the current db.session, does rollback on failure."""
        from sqlalchemy.exc import IntegrityError
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

    def delete(self):
        """Deletes this model from the db (through db.session)"""
        db.session.delete(self)
        self.__commit()

    def save(self):
        """Adds this model to the db (through db.session)"""
        db.session.add(self)
        self.__commit()
        return self

    @classmethod
    def from_dict(cls, model_dict):
        return cls(**model_dict).save()


class User(UserMixin, db.Model, BaseModel):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column('username', db.String(64), unique=True)
    _email = db.Column('email', db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        if self.is_admin:
            return '<Admin {0}>'.format(self.username)
        return '<User {0}>'.format(self.username)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        is_valid_length = check_length(username, 64)
        if not is_valid_length or not bool(USERNAME_REGEX.match(username)):
            raise ValueError('{} is not a valid username'.format(username))
        self._username = username

    username = synonym('_username', descriptor=username)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not check_length(email, 64) or not bool(EMAIL_REGEX.match(email)):
            raise ValueError('{} is not a valid email address'.format(email))
        self._email = email

    email = synonym('_email', descriptor=email)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        if not bool(password):
            raise ValueError('no password given')

        hashed_password = generate_password_hash(password)
        if not check_length(hashed_password, 128):
            raise ValueError('not a valid password, hash is too long')
        self.password_hash = hashed_password

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def seen(self):
        self.last_seen = datetime.utcnow()
        return self.save()

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'create_time': self.create_time,
            'last_seen': self.last_seen,
        }

    def promote_to_admin(self):
        self.is_admin = True
        return self.save()


@login_manager.user_loader
def load_user(user_id):
    """
    加载用户回调函数
    :param user_id:
    :return:
    """
    return User.query.get(int(user_id))


class Question(db.Model, BaseModel):
    __tablename__ = 't_question'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text(1024))
    answers_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.utcnow())

    author_id = db.Column(db.Integer, db.ForeignKey("t_user.id", ondelete="CASCADE"))  # 级联删除
    author = db.relationship("User", backref=db.backref(
        "t_question", lazy="dynamic"), uselist=False)

    def __init__(self, **kwargs):
        super(Question, self).__init__(**kwargs)


class Answer(db.Model, BaseModel):
    __tablename__ = 't_answer'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(1024))
    comments_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.utcnow())

    author_id = db.Column(db.Integer, db.ForeignKey("t_user.id", ondelete="CASCADE"))
    author = db.relationship("User", backref=db.backref(
        "t_answer", lazy="dynamic"), uselist=False)

    question_id = db.Column(db.Integer, db.ForeignKey("t_question.id"))
    question = db.relationship("Question", backref=db.backref(
        "t_answer", lazy="dynamic"), uselist=False)

    def __init__(self, **kwargs):
        super(Answer, self).__init__(**kwargs)


class Comment(db.Model, BaseModel):
    __tablename__ = 't_comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(1024))
    create_time = db.Column(db.DateTime, default=datetime.utcnow())

    author_id = db.Column(db.Integer, db.ForeignKey("t_user.id", ondelete="CASCADE"))
    author = db.relationship("User", uselist=False)

    answer_id = db.Column(db.Integer, db.ForeignKey("t_answer.id"))
    answer = db.relationship("Answer", backref=db.backref(
        "t_comment", lazy="dynamic"), uselist=False)

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)
