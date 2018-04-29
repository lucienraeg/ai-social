from flask import render_template, redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/feed')
def feed():
    new_user = {'username': 'frank'}
    posts = [
        {
            'author': {'username': 'jeff'},
            'date': '8:25 AM 11-7-18',
            'body': 'I like the number seven.'
        },
        {
            'author': {'username': 'susan'},
            'date': '11:30 PM 21-8-18',
            'body': 'Weetbix is pretty great! Here are some more words... yes!\
            El gobierno quiere comer todos los gatos.'
        }
    ]

    return render_template('feed.html', title='Feed', new_user=new_user, posts=posts)
