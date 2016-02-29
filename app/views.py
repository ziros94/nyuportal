from flask import render_template, Blueprint

nyu = Blueprint("nyu", __name__)

@nyu.route('/')
def home():
	return render_template('home.html')
