"""seed file to populate db"""

from models import User, Post, Tag, PostTag, db
from app import app

# drop and create tables
db.drop_all()
db.create_all()

# empty tables
User.query.delete()
Post.query.delete()

# Add users
gregory = User(first_name='Gregory', last_name='Marsh', image_url='https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60')
darcy = User(first_name='Darcy', last_name='Praw', image_url='https://images.unsplash.com/photo-1534361960057-19889db9621e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60')
laurie = User(first_name='Laurie', last_name='Fenamore', image_url='https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60')
ryan = User(first_name='Ryan', last_name='Riedy', image_url='https://images.unsplash.com/photo-1552053831-71594a27632d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60')
mark = User(first_name='Mark', last_name='Da La Torre', image_url='https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60')

# Add new object to sessiohn, so they will presist 
db.session.add(gregory)
db.session.add(darcy)
db.session.add(laurie)
db.session.add(ryan)
db.session.add(mark)

# commit to the db to get saved
db.session.commit()

# Add posts
post1 = Post(title='Breakfast', content='I like breakfast', user_id=1)
post2 = Post(title='Na breakfast suxs', content='I like lunch bro', user_id=2)
post3 = Post(title='Pics of Dogs', content='More pics of dogs', user_id=3)
post4 = Post(title='Dr. Strange', content='STEVE!', user_id=4)
post5 = Post(title='Wabba Lubba Dub Dub', content="Im simple rick!", user_id=5)

db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)
db.session.add(post5)

# commit to the db to get saved
db.session.commit()

#add tags

tag1 = Tag(name="Hey you")
tag2 = Tag(name="Awesome")
tag3 = Tag(name="LIke")
tag4 = Tag(name="First post!")
tag5 = Tag(name="wubba lubba dub dub")

# add and commit
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.add(tag4)
db.session.add(tag5)

db.session.commit()

#PostTag model
data1 = PostTag(post_id=1, tag_id=1)
data2 = PostTag(post_id=2, tag_id=2)
data3 = PostTag(post_id=3, tag_id=3)
data4 = PostTag(post_id=4, tag_id=4)
data5 = PostTag(post_id=5, tag_id=5)

#add and commit
db.session.add(data1)
db.session.add(data2)
db.session.add(data3)
db.session.add(data4)
db.session.add(data5)

db.session.commit()