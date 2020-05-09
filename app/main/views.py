from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Comment,Quote,Blog,Subscriber
from .forms import CommentForm,NewBlog
from .. import db,photos
from flask_login import login_required,current_user
from ..requests import get_quote 

@main.route('/')
def index():
  '''
  view root that returns the index page with the various blogs
  '''
  title = 'Blogs'
  quote=get_quote()
  blogs=Blog.query.all()
  return render_template('index.html',title=title,quote=quote,blogs=blogs)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def add_blog():
  '''
  view function for creating new blogs
  '''
  form = NewBlog()
  if form.validate_on_submit():
    title = form.title.data
    blog = form.blog.data

    # Updated blog instance
    new_pitch = Blog(title=title,content=content, user = current_user)

    # Save pitch method
    new_pitch.save_blog()
    return redirect(url_for('.index'))

  title = 'New Blog'
  return render_template('newblog.html',title = title,blog_form=form)  

@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
  '''
  view function for showing one particular blog and its comments
  '''
  blog = Blog.get_blog(id)
  comment_form = CommentForm()
  if comment_form.validate_on_submit():
    comment = comment_form.text.data

    new_comment = Comment(content = comment,user = current_user,blog_id = blog.id)

    new_comment.save_comment()
  comments = Blog.get_comments(blog)

  return render_template("blog.html", , comment_form = comment_form, comments = comments)  