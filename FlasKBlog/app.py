from flask import Flask, render_template
import requests

# fake post from apis
posts = requests.get("https://api.npoint.io/493622f5077bee2314fa").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_post=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
