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
        self.assertEqualsw(user.last_name, 'Drew')
    
    def test_delete(self):
        Drewdog = User(first_name= "Nancy", last_name="Drew", url="https://i.pinimg.com/564x/3b/59/f5/3b59f5306f2492393cbd0ac00e28c2aa.jpg")
        self.assertEqualsw(user.last_name, 'Drew')

        User.query.filter_by(name=57)