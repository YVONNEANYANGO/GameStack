from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Game, Comment
from wtforms.validators import Required,Email
from wtforms.validators import DataRequired
from ..models import Subscriber
from wtforms import ValidationError




class GameForm(FlaskForm):
    title = StringField('Games', validators=[DataRequired()])
    body = TextAreaField('add favorite games', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    title = StringField('Enter Your Name' ,validators=[Required()])
    submit = SubmitField('Subscribe')
    
    def validate_email(self,data_field):
            if Subscriber.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

