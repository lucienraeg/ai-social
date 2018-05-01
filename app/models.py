from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)

    # relationships
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    votes = db.relationship('Vote', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def posts_reversed(self):
        return list(reversed(list(self.posts)))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    upvotes = db.Column(db.Integer, index=True, default=0)
    downvotes = db.Column(db.Integer, index=True, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # relationships
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    votes = db.relationship('Vote', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def relative_timestamp(self):
        diff = datetime.utcnow() - self.timestamp
        s = diff.seconds
        if diff.days > 7 or diff.days < 0: return d.strftime('%d %b %y')
        elif diff.days == 1: return '1 day ago'
        elif diff.days > 1: return '{} days ago'.format(diff.days)
        elif s <= 1: return 'just now'
        elif s < 60: return '{} seconds ago'.format(s)
        elif s < 120: return '1 minute ago'
        elif s < 3600: return '{} minutes ago'.format(s/60)
        elif s < 7200: return '1 hour ago'
        else: return '{} hours ago'.format(s/3600)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sway = db.Column(db.Integer, index=True) # -1 or 1
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Vote {}>'.format(self.sway)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Comment {}>'.format(self.body)


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

def add_comment(post, author, body):
    c = Comment(post=post, author=author, body=body)
    db.session.add(c)
    db.session.commit()
    print('Added {} to db'.format(c))
    return c

def upvote_post(post, author):
    post.upvotes += 1
    v = Vote(post=post, author=author, sway=1)
    db.session.add(v)
    db.session.commit()

def downvote_post(post, author):
    post.downvotes += 1
    v = Vote(post=post, author=author, sway=-1)
    db.session.add(v)
    db.session.commit()

def clear_all():
    users = User.query.all()
    for u in users:
        db.session.delete(u)

    posts = Post.query.all()
    for p in posts:
        db.session.delete(p)

    votes = Vote.query.all()
    for v in votes:
        db.session.delete(v)

    comments = Comment.query.all()
    for c in comments:
        db.session.delete(c)

    db.session.commit()
    print('Cleared all')
