from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])
    submit = SubmitField('Submit')