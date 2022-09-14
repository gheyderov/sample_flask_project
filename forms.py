from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(),
        Length(min=3, max=10)
    ])
    password = StringField('password', validators=[
        DataRequired(),
        Length(min=3, max=10)
    ])



class RegisterForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(),
        Length(min=3, max=10)
    ])
    email = StringField('email', validators=[
        DataRequired(),
        Email()
    ])
    password = StringField('password', validators=[
        DataRequired(),
        Length(min=3, max=10)
    ])
    confirm_password = StringField('confirm_password', validators=[
        DataRequired(),
        Length(min=3, max=10),
        EqualTo('password')
    ])


class ContactForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(),
        Length(min=3, max=10)
    ])
    email = StringField('email', validators=[
        DataRequired(),
        Email()
    ])
    company = StringField('company', validators=[
        DataRequired(),
    ])
    message = TextAreaField('message')
    is_subscribe = BooleanField('is_subscribe')


class ReviewForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(),
        Length(min=3, max=10)
    ])
    email = StringField('email', validators=[
        DataRequired(),
        Email()
    ])
    message = TextAreaField('message')
