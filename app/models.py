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

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.now())
    status = db.Column(db.Enum('success','pending','failed'), default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))

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
    

