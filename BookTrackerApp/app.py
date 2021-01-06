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
    # read all the record and show in the home page
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # create records
        new_book = Book(
            title=request.form["title"].title(),
            author=request.form["author"].title(),
            rating=request.form["rating"].title()
        )
        # save record into db
        db.session.add(new_book)
        # commit the db
        db.session.commit()
        # after submission success then return home page
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # update the record
        book_id = request.form["id"]
        # get the book id
        book_to_update = Book.query.get(book_id)
        # update the rating
        book_to_update.rating = request.form["rating"]
        # commit into db
        db.session.commit()
        # after update go back to home
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    # select the specific book
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete():
    # grab the book id from db
    book_id = request.args.get('id')

    # delete the record from db
    # checking the id with db
    book_to_delete = Book.query.get(book_id)
    # delete the book if id match
    db.session.delete(book_to_delete)
    # commit the changes in db
    db.session.commit()
    # go back to home page
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
