from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp, EqualTo, ValidationError
from application.models.user import User

__all__ = ['LoginForm', 'RegisterForm']


class LoginForm(FlaskForm):
    email_or_username = StringField('Email or Username', validators=[InputRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    username = StringField('Username',
                           validators=[InputRequired(), Length(1, 64),
                                       Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                              message='Username should only consist of letters, numbers or _')]
                           )
    password = PasswordField(
        'Password', validators=[
            InputRequired(),
            EqualTo('password_confirmation', message='Passwords must match.')
        ]
    )

    password_confirmation = PasswordField('Confirm Password', validators=[
        InputRequired()
    ])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.objects(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.objects(username=field.data).first():
            raise ValidationError('Username already in use.')
