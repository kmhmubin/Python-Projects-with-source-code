from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

# secret key
app.secret_key = b'\xb9\xd6\xc7\xc4\xb5\xf0\xc4y\xc6\xb0\r\xc3`!\xca~'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
