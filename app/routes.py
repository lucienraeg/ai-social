from flask import render_template, redirect, url_for, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
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

    return render_template('home.html', title='home', posts=posts)