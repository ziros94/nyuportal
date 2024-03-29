from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Length, InputRequired, Email

class signinForm(Form):
    email = StringField('Email:', validators=[InputRequired(message="This field is required"), Email(message="Not a valid email")])
    password = PasswordField('Password:', validators=(InputRequired(message="This field is required"), Length(min=6, message="Password must be at least 6 characters")))
    submit = SubmitField('Login')


class newPostForm(Form):
    title = StringField('Title', validators=[InputRequired(message="This field is required")])
    description = TextAreaField('Description', validators=[InputRequired(message="This field is required")])
    submit = SubmitField('Submit')


class categoryForm(Form):
    category = StringField('Category', validators=[InputRequired(message="This field is required")])
    submit = SubmitField('Submit')



