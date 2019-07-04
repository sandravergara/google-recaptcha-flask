from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, validators

class RegisterForm(Form):
      name = StringField('Name', [validators.DataRequired(), validators.Length(max=255)])
      password = PasswordField('New Password', [validators.DataRequired(), validators.Length(min=8)])
      email = StringField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=35)])
      recaptcha = RecaptchaField()
