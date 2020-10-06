# pylint: disable=missing-docstring

from flask import Flask, render_template, request, session
from flask_session import Session
from game import Game

app = Flask(__name__)
SESSION_TYPE='filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    score = session.get('score', 0)
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form["word"]
    is_valid = game.is_valid(word)

    if is_valid:
        session['score'] = session.get('score', 0) + 1

    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)
