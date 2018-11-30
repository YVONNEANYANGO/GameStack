from flask import render_template,redirect,url_for
# from ..models import Chat
# from .forms import SubscriberForm
from . import main

@main.route('/')
def index():
    return render_template('home.html') 

@main.route('/', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber=Subscriber(email=subscriber_form.email.data,title= subscriber_form.title.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message('Welcome to GameStack App')
  
