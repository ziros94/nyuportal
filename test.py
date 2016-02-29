import os
from app import app, db
from app.models import User, Post
 
db.drop_all()
db.create_all()

_basedir = os.path.abspath(os.path.dirname(__file__))

print Post.query.all()
print User.query.all()
