from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

# secret key
app.secret_key = b'\xb9\xd6\xc7\xc4\xb5\xf0\xc4y\xc6\xb0\r\xc3`!\xca~'

Bootstrap(app)

# creating db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# creating table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# edit the rating and reviews

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route('/')
def home():
    # get all the movies from DB
    all_movies = Movie.query.all()
    return render_template('index.html', movies=all_movies)


@app.route('/edit', methods=["GET", "POST"])
def rate_movie():
    # inherit form the class
    form = RateMovieForm()
    # get the id
    movie_id = request.args.get('id')
    # check with db
    movie = Movie.query.get(movie_id)
    # if the id match then update
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


if __name__ == '__main__':
    app.run()
