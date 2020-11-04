"""seed file to populate db"""

from models import User,db
from app import app

# drop and create tables
db.drop_all()
db.create_all()

# empty tables
db.query.delete()

# Add users
gregory = User(first_name='Gregory', last_name='Marsh', image_url='www.google.com')
darcy = User(first_name='Darcy', last_name='Praw', image_url='www.google.com')
laurie = User(first_name='Laurie', last_name='Fenamore', image_url='www.google.com')
ryan = User(first_name='Ryan', last_name='Riedy', image_url='www.google.com')
mark = User(first_name='Mark', last_name='Da La Torre', image_url='www.google.com')

# Add new object to sessiohn, so they will presist 
db.session.add(gregory)
db.session.add(darcy)
db.session.add(laurie)
db.session.add(ryan)
db.session.add(mark)

# commit to the db to get saved
db.session.commit()