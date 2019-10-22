from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required])
    password = PasswordField('Password', validators=[Required])
    submit = SubmitField('log in')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[Required])
    password = PasswordField('Password', validators=[Required])
    confirm_password = PasswordField('Repeat password', validators=[EqualTo(password)])
    submit = SubmitField('sign in')
