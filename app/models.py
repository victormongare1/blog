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