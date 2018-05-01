from datetime import datetime
from flask import render_template, redirect, url_for, request
import models
from app import app

'''
models.clear_all()

u = models.add_user('tim')
models.add_post(u, 'Yo whas poopin bois')
models.add_post(u, 'We all good in the hood')

u = models.add_user('samantha')
models.add_post(u, 'Look it\'s time for some words... El gobierno quiere comer \
todos las gatos! No esta en melbourne, god it can be difficult to write about nothing')

u = models.add_user('john')
models.add_post(u, 'How are we all today? I just thinks it\'s fantastic that we \
can all enjoy citrus fruit.')

p = models.Post.query.get(3)
models.upvote_post(p)

p = models.Post.query.get(2)
models.downvote_post(p)

u = models.User.query.get(2)
p = models.Post.query.get(4)
models.add_comment(p, u, 'This is a comment')
'''


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    posts = list(reversed(models.Post.query.all()))

    return render_template('home.html', title='home', posts=posts)

@app.route('/users')
def users():
    users = models.User.query.all()
    return render_template('users.html', title='users', users=users)

@app.route('/user/<userid>')
def user(userid):
    user = models.User.query.get(userid)
    return render_template('user.html', title=user.username, user=user)
