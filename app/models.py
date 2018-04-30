from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

def add_user(username):
    u = User(username=username)
    db.session.add(u)
    db.session.commit()
    print('Added {} to db'.format(u))
    return u

def add_post(author, body):
    p = Post(body=body, author=author)
    db.session.add(p)
    db.session.commit()
    print('Added {} to db'.format(p))
    return p

def clear_users():
    users = User.query.all()
    for u in users:
        db.session.delete(u)
    db.session.commit()
    print('Cleared users')

def clear_posts():
    posts = Post.query.all()
    for p in posts:
        db.session.delete(p)
    db.session.commit()
    print('Cleared posts')
