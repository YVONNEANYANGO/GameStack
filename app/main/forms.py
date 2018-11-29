from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Game, Comment
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    title = StringField('Favorite Games', validators=[DataRequired()])
    body = TextAreaField('add latest games', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment', validators=[DataRequired()])
    submit = SubmitField('Submit')
