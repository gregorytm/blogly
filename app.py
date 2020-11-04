"""Blogly application."""
from flask import Flask, request, redirect, session,render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Mario-and-Luigi-188'

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/users')
def list_users():
    return render_template('user_data.html')

# db.create_all()
