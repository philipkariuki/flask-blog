
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
        
    comments = Comment.get_comments(id)
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
        new_comment = Comment( comment_content=comment_content, post=post, user=current_user)
        new_comment.save_comment()

        return redirect(url_for('.post', id=post.id ))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)


@main.route('/writer')
@login_required
def writer():
    if current_user.role.id == 1 :

        title = 'Writer'
        posts = Post.get_posts()

        return render_template('writer.html', title = title, posts=posts )

    else:
        abort(404)






@main.route('/writer/post/new', methods=['GET','POST'])
@login_required
def new_post():
    if current_user.role.id == 1 :

        form = PostForm()

        if form.validate_on_submit():
            post_title = form.post_title.data
            post_content = form.post_content.data
            new_post = Post(post_title=post_title, post_content=post_content, user=current_user)
            new_post.save_post()
            subscribers = User.get_subscribers()
            subscribers = ",".join(subscribers)
            mail_message("New post in the C blog","email/update_user",subscribers)

            return redirect(url_for('.writer'))

        title = 'Create Post'

        return render_template('new_post.html', title = title, post_form=form )

    else:
        abort(404)

@main.route('/writer/post/<int:id>')
@login_required
def writer_post(id):
    if current_user.role.id == 1 :

        post = Post.query.get(id)
        title = f'Post {post.id}'
        comments = Comment.get_comments(id)


        return render_template('writer_post.html', title = title, post=post, comments=comments )

    else:
        abort(404)

@main.route('/writer/post/comment/delete/<int:id>')
@login_required
def delete_comment(id):

    if current_user.role.id == 1:

        comment = Comment.query.get(id)
        comment.delete_single_comment(id)

        return redirect(url_for('.writer'))

    else:
        abort(404)

@main.route('/writer/post/delete/<int:id>')
@login_required
def delete_post(id):

    if current_user.role.id == 1:

        post = Post.query.get(id)

        post.delete_post(id)

        return redirect(url_for('.writer'))


    else:
        abort(404)

@main.route('/writer/post/update/<int:id>' , methods=['GET','POST'])
@login_required
def update_post(id):

    if current_user.role.id == 1:

        current_post = Post.query.get(id)

        form = PostForm(obj=current_post)

        if form.validate_on_submit():
            
            form.populate_obj(current_post)

            comments = Comment.query.filter_by(post_id=id).all()
            post = Post.query.filter_by(id=id).update({
                'post_title': form.post_title.data, 
                'post_content': form.post_content.data
                })
            db.session.commit()

            return redirect(url_for('.writer'))

        title = 'Update Post'

        return render_template('update_post.html', title = title, update_post_form=form )

    else:
        abort(404)




@main.route('/subscribe/<int:id>')
@login_required
def subscribe(id):
    '''
    View subscribe function that allows a user to subscribe for email updates when new post is posted
    '''
    user = User.query.get(id)

    if user is None:
        abort(404)

    user.subcribe_user(id)
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



