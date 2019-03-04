from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp, Email, EqualTo, ValidationError
from application.models.user import User

__all__ = ['RegisterForm', 'LoginForm']


class LoginForm(FlaskForm):
    email_or_username = StringField('Email or Username', validators=[
        InputRequired(), Length(1, 64)
    ])
    password = PasswordField('Password', validators=[
        InputRequired()
    ])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[
            InputRequired(), Length(1, 64),
            Regexp('^[A-Za-z][A-Za-z0-9_]*$',
            message='Username should only consist of letters, numbers or _')
        ]
    )
    email = StringField(
        'Email', validators=[
            InputRequired(), Length(1, 64), Email()
        ]
    )
    password = PasswordField(
        'Password', validators=[
            InputRequired(), EqualTo('password_confirm', message='Password must match.')
        ]
    )

    password_confirm = PasswordField(
        'Confirm Password', validators=[
            InputRequired()
        ]
    )

    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.objects(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.objects(username=field.data).first():
            raise ValidationError('Username already registered.')
