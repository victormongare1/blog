from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo,email_validator
from ..models import User,Subscriber
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
  '''
  wtf form for writer to register
  '''
  email = StringField('Your Email Address',validators=[Required(),Email()])
  username = StringField('Enter your username',validators = [Required()])
  password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
  password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
  submit = SubmitField('Sign Up')
  def validate_email(self,data_field):
    if User.query.filter_by(email =data_field.data).first():
      raise ValidationError('There is an account with that email')
  def validate_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('That username is taken')  
    
class LoginForm(FlaskForm):
  '''
  wtf form for writer to login
  '''
  email = StringField('Your Email Address',validators=[Required(),Email()])
  password = PasswordField('Password',validators =[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Sign In')

class SubscribeForm(FlaskForm):
  '''
  wtf form for user to subscribe
  '''
  username=StringField('Enter your username',validators = [Required()])
  email = StringField('Your Email Address',validators=[Required(),Email()])
  submit = SubmitField('Sign Up')
  def validate_email(self,data_field):
    if Subscriber.query.filter_by(email =data_field.data).first():
      raise ValidationError('There is an account with that email')
  def validate_username(self,data_field):
    if Subscriber.query.filter_by(username = data_field.data).first():
      raise ValidationError('That username is taken')  