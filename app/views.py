from flask import render_template, Blueprint, request, redirect, url_for
from .models import User
from .forms import signinForm

nyu = Blueprint("nyu", __name__)


@nyu.route('/')
def home():
    return render_template('home.html')


#TODO fix password checking
@nyu.route('/login', methods=['GET', 'POST'])
def login():
    form = signinForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email, password=password).first()
        if user is not None:
            return redirect(url_for('/'))
    return render_template('login.html', sForm=form)
