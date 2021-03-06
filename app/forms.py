from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField
    )
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    ValidationError,
    Length
    )
from app.models import User


class LoginForm(FlaskForm):
    "Form to take user login data"
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Get In")

class RegistrationForm(FlaskForm):
    "Form to handle registration"
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
        )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("This user name is already taken. Choose different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This email address is already registered. Provide different address.")

class EditProfileForm(FlaskForm):
    "Form to edit users' profile information"
    username = StringField("Username", validators=[DataRequired()])
    about_me = TextAreaField("About me", validators=[Length(min=0, max=140)])
    submit = SubmitField("Submit")

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError("Please, use different username.")

class PostForm(FlaskForm):
    "Form to submit posts"
    post = TextAreaField("Say something", validators=[DataRequired(),
                            Length(min=1, max=140)])
    submit = SubmitField("Submit")

