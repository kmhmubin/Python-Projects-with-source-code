from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = b'\xeb\x8b!\x9c\x8cF}\xa0\xa3:\xe4f\xe9\xc7\xc4\x9b'

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
# silence the deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# connecting the database with flask app
db = SQLAlchemy(app)


# Creating table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# create the database
db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # create records
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        # save record into db
        db.session.add(new_book)
        # commit the db
        db.session.commit()
        # after submission success then return home page
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run()
