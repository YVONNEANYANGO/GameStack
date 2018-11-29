from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required, current_user
from .forms import GameForm, CommentForm
from ..models import User,Game, Comment
from ..import db

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    return render_template('index.html')
    
@main.route('/game/new', methods=["GET", "POST"])
@login_required
def new_Game():
    form = GameForm()
    if form.validate_on_submit():
        game = Game(title = form.title.data, body = form.body.data)
        db.session.add(game)
        db.session.commit()
        flash('You can add some favorite games')
        return redirect(url_for('main.new_Game'))
    title = "View Games"
    games = Game.query.all()

    return render_template('game.html', title=title, form=form, game_list=games)


@main.route('/comment/new/<game_id>', methods = ["GET", "POST"])
@login_required
def new_comment(game_id):
    game = Game.query.filter_by(id = game_id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(comment=comment_form.comment.data, main_game = game)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been succesfully posted')
        return redirect(url_for('main.new_Game'))
    comments = Comment.query.all()
    return render_template('form.html', comment_form=comment_form, comment_list=comments)



