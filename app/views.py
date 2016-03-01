from flask import render_template, Blueprint, request, redirect, url_for
from .models import User, Post, Tag, Comment, Category, StatusUpdate
from .forms import signinForm, newPostForm, categoryForm
from app import db
nyu = Blueprint("nyu", __name__)


@nyu.route('/')
def home():
    posts = Post.query.filter_by(approved=True)
    return render_template('home.html', posts=posts)

@nyu.route('/pending')
def pending():
    posts = Post.query.filter_by(approved=False, status='pending')
    return render_template('pending.html', posts=posts)

#TODO fix password checking
@nyu.route('/login', methods=['GET', 'POST'])
def login():
    form = signinForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect('/')
    return render_template('login.html', sForm=form)


@nyu.route('/newpost', methods=['GET', 'POST'])
def newpost():
    form = newPostForm(request.form)
    categories = Category.query.all()
    if form.validate_on_submit():
        rForm = request.form
        title = form.title.data
        description = form.description.data
        category = Category(rForm["category"])

        post = Post(title, description)
        post.category = category

        db.session.add(post)
        db.session.commit()

        return redirect('/pending')
    return render_template('newpost.html', form=form, categories=categories)


@nyu.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    form = categoryForm(request.form)
    if form.validate_on_submit():
        category = Category(form.category.data)
        #print category
        db.session.add(category)
        db.session.commit()
        return redirect('/home')
    return render_template('addcategory.html', form=form)


@nyu.route('/approve', methods=['POST'])
def approve():
    if request.method == 'POST':
        rform = request.form
        post = Post.query.get(rform["approve"])
        post.approved = True
        post.status = 'success'
        db.session.add(post)
        db.session.commit()
    return redirect('/')    


@nyu.route('/post/<id>')
def post(id):
    post = Post.query.get(id)
    return render_template('post.html', post=post) 
