from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

#login decorator modifies the loderuser function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#creating a class user and connecting the class to our database
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")
   

    #this decorator generates my password and passes it to the passecurecolumn 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    #method that takes ,hashes and compares our password
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'
