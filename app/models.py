from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  '''
  user class to define user objects
  '''
  __tablename__='users'

  id=db.Column(db.Integer,primary_key = True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255),unique=True,index=True)
  pass_secure=db.Column(db.String(255))
  password_hash=db.Column(db.String(255))
  
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  @password.setter
  def password(self,password):
    self.pass_secure=generate_password_hash(password)
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password) 
  def save_user(self):
    db.session.add(self)
    db.session.commit()

class Blog(db.Model):
  '''
  blog class to define blog objects
  '''
  __tablename__='blogs'

  id=db.Column(db.Integer,primary_key = True)
  title=db.Column(db.String)
  content=db.Column(db.String)
  comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Comment(db.Model):
  '''
  comment class to define comment objects
  ''' 
  __tablename__='comments'
  
  id = db.Column(db.Integer,primary_key=True)  
  content==db.Column(db.String)
  blog_id=db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)

class Subscriber(db.Model):
  '''
  comment class to define subscriber objects
  '''
  __tablename__='subscriber'

  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(255),index=True)
  email=db.Column(db.String(255),unique=True,index=True)

class Quote():
  '''
  Quote class to define quote objects
  '''
  def __init__(self,author,quote):
    self.author=author
    self.quote=quote
