from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
