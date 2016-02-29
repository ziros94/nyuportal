import os
from app import app, db
from app.models import User, Post
 
db.drop_all()
db.create_all()

_basedir = os.path.abspath(os.path.dirname(__file__))

print "Adding New User"
user = User("alchen", "password", "a@nyu.edu", "alan", "chen")
db.session.add(user)

db.session.commit()

print "User Title: " + User.query.filter_by(username='alchen').first().title

print Post.query.all()
print User.query.all()
