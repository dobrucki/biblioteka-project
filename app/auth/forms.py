from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required])
    password = PasswordField('Password', validators=[Required])
    submit = SubmitField('log in')
