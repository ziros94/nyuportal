from flask import Flask

from .models import db
from .views import nyu

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db.init_app(app)
app.register_blueprint(nyu)