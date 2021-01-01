from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


if __name__ == '__main__':
    app.run()
