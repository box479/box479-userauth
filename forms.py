from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_initial = StringField('Last Initial', validators=[
        DataRequired(),
        Length(min=1, max=1)
    ])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    role = SelectField('Role', choices=[
        ('admin', 'Admin'),
        ('pump', 'Pump'),
        ('laborer', 'Laborer'),
        ('finisher', 'Finisher')
    ], validators=[DataRequired()])

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_initial = StringField('Last Initial', validators=[
        DataRequired(),
        Length(min=1, max=1)
    ])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
