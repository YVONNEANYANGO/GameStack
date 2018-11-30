# from . import db
from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import UserMixin
# from . import login_manager
from datetime import datetime

#creating a class user and connecting the class to our database
# class User(UserMixin,db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer,primary_key = True)
#     pass_secure = db.Column(db.String(255))
#     password_hash = db.Column(db.String(255))
#     email = db.Column(db.String(255),unique = True,index = True)
#     password_secure = db.Column(db.String(255))
   

    #this decorator generates my password and passes it to the passecurecolumn 
    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')

    
    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)

    # #method that takes ,hashes and compares our password
    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)


    # def __repr__(self):
    #     return f'User {self.username}'

#class subscriber has column email for the user to receive an email after subscription
# class Subscriber(UserMixin, db.Model):
#     __tablename__="subscribers"

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255),unique = True,index = True)


#     def save_subscriber(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_subscribers(cls,id):
#         return Subscriber.query.all()
         

#     def __repr__(self):
#         return f'User {self.email}'
