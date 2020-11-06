from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""
class User(db.Model):
    __tablename__ = 'users'

    @classmethod
    def get_by_users(cls, first_name, last_name):
        return cls.query.filter_by(first_name=first_name,last_name=last_name).all()
    
    def __repr__(self):
        u = self
        return f"<User id={u.id} first name={u.first_name} last name = {u.last_name} pic = {u.image_url}>"
    """user"""

    id = db.Column(db.Integer, 
                 primary_key=True,
                 autoincrement=True)

    first_name = db.Column(db.String(50), 
                          nullable=False, 
                          unique=True)

    last_name = db.Column(db.String(50), 
                        nullable=False, 
                        unique=True)

    image_url = db.Column(db.String(150), 
                        nullable=True, 
                        unique=False)

