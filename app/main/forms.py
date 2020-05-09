from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

class CommentForm(FlaskForm):
  '''
  class to define wtf form for comments
  '''
  text = TextAreaField('Leave a comment:',validators=[Required()])
  submit=SubmitField('Submit')

class NewBlog(FlaskForm):
  '''
  class to define wtf form for blogs
  '''
  title = StringField("Blog Title", validators = [Required()])
  content = TextAreaField("Content", validators = [Required()])
  submit=SubmitField("Create Blog")