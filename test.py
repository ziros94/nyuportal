import os
from app import app, db
from app.models import User, Post, Tag
 
db.drop_all()
db.create_all()

_basedir = os.path.abspath(os.path.dirname(__file__))
print "\n\n===================\n"
print "Adding New User"
user = User("alchen", "password", "a@nyu.edu", "alan", "chen")
print 'Adding new post'
post = Post('test_post1', 'this is a test post number 1')
user.posts.append(post)
print 'Adding tags'
tags = [Tag('healthcare'), Tag('tuition')]
post.tags+=tags
db.session.add(user)

db.session.commit()

user = User.query.filter_by(username='alchen').first()
print "User Title: " + user.title
for post in user.posts:
    print post
    for tag in post.tags:
        print tag
print "======================\n"
print User.query.all()
print Post.query.all()
print Tag.query.all()
