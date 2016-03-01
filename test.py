import os
from app import app, db
from app.models import User, Post, Tag, Comment, Category, StatusUpdate
 
db.drop_all()
db.create_all()

_basedir = os.path.abspath(os.path.dirname(__file__))
print "\n\n===================\n"
print "Adding New User"
user = User("a@nyu.edu", "password", "alan", "chen")
print "Adding new Category"
category = Category("Healthcare")

db.session.add(user)
db.session.add(category)
db.session.commit()

print 'Adding new post'
post = Post('test_post1', 'this is a test post number 1')
print 'Adding tags'
tags = [Tag('healthcare'), Tag('tuition')]
post.tags+=tags
post.user = user
post.category = category
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
    comment.upvotes.append(user)
    db.session.add(comment)
db.session.commit()    
for signature in post.signatures:
    print 'Signature: ' + str(signature)

comment = Comment.query.first()
for upvote in  comment.upvotes:
    print "Upvoted by User: " + str(upvote)
print post.title + "'s Category: " + str(post.category)
print "======================\n"
print User.query.all()
print Category.query.all()
print Post.query.all()
print Tag.query.all()
print Comment.query.all()
