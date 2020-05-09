from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Comment,Quote
from .forms import UpdateProfile,NewPitch,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
from ..requests import get_quote 

@main.route('/')
def index():
  '''
  view root that returns the index page and various news sources 
  '''
  title = 'Blogs'
  quote=get_quote()
  return render_template('index.html',title=title,quote=quote)