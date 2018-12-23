# coding=utf-8
from . import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "duke"}
    posts = {
            "author":{"username":"刘"},
            "body":"这是模板中的循环例子1"
        }

    return render_template('index.html', title='我的', user=user, posts=posts)
