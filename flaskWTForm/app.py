from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


# creating a form

class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label="Login")


app = Flask(__name__)
# app secret key
app.secret_key = b'1\xadL~]\x8e2\xe4\xf6\xa6\xe0\xefWL\xb1\x92'


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run()
