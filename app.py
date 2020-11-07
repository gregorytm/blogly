"""Blogly application."""
from flask import Flask, request, redirect, session, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Mario-and-Luigi-188'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    return redirect('/users')

@app.route('/users')
def list_users():
    users=User.query.all()
    return render_template('user_data.html', users=users)

@app.route('/users/new')
def add_page():
    return render_template('new.html')

@app.route('/users/new', methods=["POST"])
def create_user():
    first_name=request.form["first"]
    last_name=request.form["last"]
    image_url=request.form['url']
    
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """show details about one user"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/users/<int:user_id>/edit')
def edit_page(user_id):
    """show edit form"""
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def submit_update(user_id):
    first=request.form["first"]
    last=request.form["last"]
    if len(url) == 0:
        url = None
    else:
        url=request.form["url"]
    user = User.query.get_or_404(user_id)
    user.first_name = first
    user.last_name = last
    user.image_url = url
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    user=User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return redirect('/users')

# db.create_all()
