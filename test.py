import os
from app import app, db
from app.models import User, Post, Tag, Comment
 
db.drop_all()
db.create_all()

_basedir = os.path.abspath(os.path.dirname(__file__))
print "\n\n===================\n"
print "Adding New User"
user = User("alchen", "password", "a@nyu.edu", "alan", "chen")
print 'Adding new post'
post = Post('test_post1', 'this is a test post number 1')

print 'Adding tags'
tags = [Tag('healthcare'), Tag('tuition')]
post.tags+=tags
user.posts.append(post)
db.session.add(user)

db.session.commit()

comment = Comment("test comment")
comment2 = Comment("test comment")
user = User.query.filter_by(username='alchen').first()
post = Post.query.filter_by(user_id=user.id).first()
post.comments.append(comment)
post.comments.append(comment2)
user.comments.append(comment)
user.comments.append(comment2)
post.signatures.append(user)
db.session.add(user)
db.session.add(post)
db.session.commit()

print "User Title: " + user.title
print "Post Title: " + post.title
for comment in user.comments:
    print user.username + "'s Comment: " + str(comment)
    print comment.user.id
for comment in post.comments:
    print post.title + "'s Comment: " + str(comment)
    print comment.post.id
for signature in post.signatures:
    print 'Signature: ' + str(signature)

print "======================\n"
print User.query.all()
print Post.query.all()
print Tag.query.all()
print Comment.query.all()
