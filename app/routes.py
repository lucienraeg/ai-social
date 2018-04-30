from datetime import datetime
from flask import render_template, redirect, url_for, request
import models
from app import app

'''
models.clear_users()
models.clear_posts()

u = models.add_user('tim')
models.add_post(u, 'Yo whas poopin bois')
models.add_post(u, 'We all good in the hood')

u = models.add_user('samantha')
models.add_post(u, 'How are we all today?')
'''

'''
u = models.User.query.get(1)
models.add_post(u, 'Question: is a hot dog a sandwich? Discuss.')
'''

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    posts = list(reversed(models.Post.query.all()))
    disp_posts = []

    return render_template('home.html', title='home', posts=posts)

@app.route('/users')
def users():
    users = models.User.query.all()
    return render_template('users.html', title='users', users=users)

@app.route('/user/<userid>')
def user(userid):
    user = models.User.query.get(userid)
    return render_template('user.html', title=user.username, user=user)
