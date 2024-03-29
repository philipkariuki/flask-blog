from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='user', lazy='dynamic')
    subscribe = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

    @classmethod
    def check_role(cls,user_id,role_id):
        get_role = User.query.filter_by(id=user_id).filter_by(role_id=role_id).first()
        return get_role

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def subcribe_user(cls,user_id):
        user = User.query.filter_by(id=user_id).update({
            'subscribe':True
            })
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        users = User.query.filter_by(subscribe=True).all()
        users_emails = []
        for user in users:
            users_emails.append(user.email)
        return users_emails


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'


class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.String)
    post_date = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comments', backref='post', lazy='dynamic', cascade="all, delete-orphan")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = Post.query.order_by(Post.id.desc()).all()
        return posts

    @classmethod
    def delete_post(cls,post_id):
        comments = Comment.query.filter_by(post_id=post_id).delete()
        post = Post.query.filter_by(id=post_id).delete()
        db.session.commit()



class Comments(db.Model):
    __tablename__ = 'comments'

    # table columns
    id = db.Column(db. Integer,primary_key = True)
    comment_content = db.Column(db.String)
    date_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id",ondelete='CASCADE') )

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(post_id=id).all()
        return comment

    @classmethod
    def delete_single_comment(cls,comment_id):
        comment = Comments.query.filter_by(id=comment_id).delete()
        db.session.commit()
 

    