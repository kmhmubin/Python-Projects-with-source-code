from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = b'\xeb\x8b!\x9c\x8cF}\xa0\xa3:\xe4f\xe9\xc7\xc4\x9b'

# all books list

all_books = []


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
