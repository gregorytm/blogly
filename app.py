"""Blogly application."""
from flask import Flask, request, redirect, session, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

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
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('posts/homepage.html', posts=posts)

@app.route('/users')
def list_users():
    users=User.query.all()
    return render_template('users/list_users.html', users=users)

@app.route('/users/new')
def add_page():
    return render_template('users/new_user.html')

@app.route('/users/new', methods=["POST"])
def create_user():
    first_name=request.form["first"]
    last_name=request.form["last"]
    image_url=request.form['url']

    if len(image_url) <= 0:
        image_url = None
    
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """show details about one user"""
    user = User.query.get_or_404(user_id)
    return render_template("users/details.html", user=user)


##user edit routes
@app.route('/users/<int:user_id>/edit')
def edit_page(user_id):
    """show edit form"""
    user = User.query.get_or_404(user_id)
    return render_template("users/edit.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def submit_update(user_id):
    first=request.form["first"]
    last=request.form["last"]
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
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

#########Post routes

@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    """show post form"""
    user = User.query.get_or_404(user_id)
    return render_template("posts/posts_new.html", user=user)

###new
@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def new_post(user_id):
    """submit post"""
    user=User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'],
        content=request.form['content'],
        user=user)
   
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f"/users/{user_id}")

###show info
@app.route('/posts/<int:post_id>')
def posts_show(post_id):
    """Show a page with info on a specific post"""

    post = Post.query.get_or_404(post_id)
    return render_template('posts/show.html', post=post)

###edit routes
@app.route('/posts/<int:post_id>/edit')
def edit_form(post_id):
    """edit form"""
    post=Post.query.get_or_404(post_id)
    return render_template('posts/edit.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def edit_post(post_id):
    """edit post in DB"""
    post=Post.query.get_or_404(post_id)
    post.title=request.form['title']
    post.content=request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """"delete post"""

    post=Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")



# db.create_all()
