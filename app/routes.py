from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Vaidas"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Vilnius!"
        },
        {
            "author": {"username": "Susan"},
            "body": "Dragon Ball Super rocks!"
        }
    ]

    return render_template('index.html', title="Home", user=user, posts=posts)