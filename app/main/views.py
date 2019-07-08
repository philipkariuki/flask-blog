
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import CommentForm,UpdateProfile,PostForm
from ..models import User, Post,Comments, Role
from flask_login import login_required, current_user
from .. import db,photos
import markdown2




@main.route('/')
def index():
    
    posts = Post.get_posts()
    title = 'Phil Blog'
    return render_template('index.html', title = title, posts = posts )




@main.route('/post/<int:id>')
def post(id):

    post = Post.query.get(id)

    if post is None:
        abort(404)
        
    comments = Comments.get_comments(id)
    title = "Posts"
    return render_template('post.html', title=title, post=post, comments=comments )



@main.route('/post/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):

    form = CommentForm()
    post = Post.query.filter_by(id=id).first()

    if post is None:
        abort(404)

    

    if form.validate_on_submit():
        comment_content = form.comment_content.data
        new_comment = Comments( comment_content=comment_content, post=post, user=current_user)
        new_comment.save_comments()

        return redirect(url_for('.post', id=post.id ))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)





@main.route('/post/comment/delete/<int:id>')
@login_required
def delete_comment(id):

        comment = Comments.query.get(id)
        comment.delete_single_comment(id)

        return redirect(url_for('.index'))





@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)





@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



