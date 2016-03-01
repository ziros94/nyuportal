import os
from app import app, db
from app.models import User, Post, Tag, Comment, Category, StatusUpdate
 
db.drop_all()
db.create_all()

_basedir = os.path.abspath(os.path.dirname(__file__))
print "\n\n===================\n"
print "Adding New User"
users = [User("a@nyu.edu", "password", "alvi", "kabir"),User("b@nyu.edu", "password", "amy", "chen"),User("c@nyu.edu", "password", "sophia", "smith"),User("admin@nyu.edu", "password", "alan", "chen"),User("sarth.desai@nyu.edu", "password", "Sarth", "Desai")]
print "Adding new Category"
categories = [Category("Healthcare"),Category("Education"),Category("Tuition"),Category("Dining")]

print 'Adding new post'
post1 = Post('Terrible Dining', 'There is food poisoning epidemic because of our cafeteria food')
post1.category = categories[3]
post1.approved = True
post1.status = 'success'
post2 = Post('Need better health center', 'School needs better health services')
post2.category = categories[0]
post2.approved = True
post2.status = 'success'
post3 = Post('Tuition is too high', 'NYU needs to lower tuition')
post3.category = categories[2]
post3.approved = True
post3.status = 'success'
post4 = Post('Classes are too hard', 'Professors need to make classes easier')
post4.category = categories[1]
post5 = Post('Tuition is too cheap', 'Tuition should be higher')
post5.category = categories[2]

posts = [post1,post2,post3,post4,post5]
for i in range(len(posts)):
    posts[i].user = users[i]
    posts[i].signatures+=users
db.session.add_all(users)
db.session.add_all(categories)
db.session.add_all(posts)
db.session.commit()
'''print 'Adding tags'
tags = [Tag('healthcare'), Tag('tuition')]
post.tags+=tags
post.user = user
post.category = category
post.approved=True
comment = Comment("test comment")
comment2 = Comment("test comment")
user = User.query.filter_by(email='a@nyu.edu').first()
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
    print user.email + "'s Comment: " + str(comment)
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
print post.title + "'s Category: " + str(post.category)'''
print "======================\n"
print User.query.all()
print Category.query.all()
print Post.query.all()
#print Tag.query.all()
#print Comment.query.all()
