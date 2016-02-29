from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from .models import db
from .views import nyu

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

db.drop_all()
db.create_all()

#db.init_app(app)
app.register_blueprint(nyu)