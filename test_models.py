from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://blogly_test'
app.configt['SQLALCHEMPY_ECHO'] = False

db.drop.all()
db.create_all()

class UserModelTestCase(TestCase):
    """Test for model for User"""

    def setUp(self):
        """Clean up any existing users"""
        User.query.delete()

    def tearDown(self):
        """Clean up any leftovers"""
        db.session.rollback()
        
    def test_user(self):
        Drewdog = User(first_name= "Nancy", last_name="Drew", url="https://i.pinimg.com/564x/3b/59/f5/3b59f5306f2492393cbd0ac00e28c2aa.jpg")
        self.assertEquals(user.last_name, 'Drew')
    
    def test_user_edit(self):
        Drewdog = User(first_name= "Nancy", last_name="Drew", url="https://i.pinimg.com/564x/3b/59/f5/3b59f5306f2492393cbd0ac00e28c2aa.jpg")
        user.image_url = "https://images.unsplash.com/photo-1553258318-c22356c14808?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"


