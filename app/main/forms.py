from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import Required,Email
from ..models import Subscriber
from wtforms import ValidationError

class SubscriberForm(FlaskForm)
    email = StringField('Your Email Address',validators=[Required(),Email()])
    title = StringField('Enter Your Name',validators=[Required(),])
    submit = SubmitField('Subscribe')

def validate_email(self)