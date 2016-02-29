#  python
#  from app.models import User
#  from app import db
#

from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60))
    lastName = db.Column(db.String(60))
    title = db.Column(db.Enum('student', 'council', 'admin'), default='student')
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(54))
    email = db.Column(db.String(120), unique=True)
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    status_updates = db.relationship('StatusUpdate', backref='user', lazy='dynamic')

    def __init__(self, username, password, email, firstName, lastName):
        self.username = username
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return '<User %r>' % self.username



tags = db.Table('tags',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
        db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)
signatures = db.Table('signatures',
        db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
upvotes = db.Table('upvotes',
        db.Column('comment_id', db.Integer, db.ForeignKey('comment.id')),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.now())
    status = db.Column(db.Enum('success','pending','failed'), default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))
    signatures = db.relationship('User', secondary=signatures, backref=db.backref('posts_signed', lazy='dynamic'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic') 
    status_updates = db.relationship('StatusUpdate', backref='post', lazy='dynamic')

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Post %r>' % self.title


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Tag %r>' % self.name
   

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Category %r>' % self.name


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    upvotes = db.relationship('User', secondary=upvotes, backref=db.backref('upvoted_comments', lazy='dynamic'))

    def __init__(self, comment_text):
        self.comment_text = comment_text

    def __repr__(self):
        return '<Comment %r>' % self.comment_text


class StatusUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __init__(self, status_text):
        self.status_text = status_text
    
    def __repr__(self):
        return '<StatusUpdate %r>' % self.status_text
