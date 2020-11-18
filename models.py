import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Models for Blogly."""
class User(db.Model):
    __tablename__ = 'users'
    
    def __repr__(self):
        u = self
        return f"<User id={u.id} first name={u.first_name} last name = {u.last_name} pic = {u.image_url}>"
    """user"""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default="https://images.unsplash.com/photo-1553258318-c22356c14808?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60")

    posts = db.relationship('Post', backref ="user", cascade ="all, delete-orphan")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    """Posts Model"""
    __tablename__= 'posts'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Text, nullable=False)
    content=db.Column(db.Text, nullable=False)
    created_at=db.Column(
        db.DateTime,
        nullable = False,
        default=datetime.datetime.now)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p")

class PostTag(db.Model):
    __tablename__ = 'posts_tags'
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Tag (db.Model):
    __tablename__='tags'

    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship(
        'Post',
        secondary='posts_tags',
        backref="tags"
    )
def connect_db(app):
    db.app = app
    db.init_app(app)
