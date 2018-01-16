from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    "Form to take user login data"
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Get In")