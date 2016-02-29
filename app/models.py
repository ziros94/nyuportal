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

    def __init__(self, username, password, email, firstName, lastName):
        self.username = username
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.now())
    status = db.Column(db.Enum('success','pending','failed'))
