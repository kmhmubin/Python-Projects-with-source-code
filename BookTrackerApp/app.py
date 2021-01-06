from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = b'\xeb\x8b!\x9c\x8cF}\xa0\xa3:\xe4f\xe9\xc7\xc4\x9b'

# all books list

all_books = []

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

# connecting the database with flask app
db = SQLAlchemy(app)


# Creating table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # this allow each book object to be identify by its title
    def __repr__(self):
        return f'<Book {self.title}>'


# create the database
db.create_all()

# create the record in db
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)

db.session.add(new_book)

db.session.commit()


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"].title(),
            "author": request.form["author"].title(),
            "rating": request.form["rating"].title()
        }
        # save in the empty list
        all_books.append(new_book)
        # print(all_books)
        # after submission success then return home page
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run()
