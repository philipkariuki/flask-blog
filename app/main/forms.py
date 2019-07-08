from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    
    comment_content = TextAreaField('Insert Comment here', validators = [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
	post_title = StringField('Post Title')
    post_content = TextAreaField('Insert thoughts here', validators = [Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

