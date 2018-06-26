from flask import Flask, request, render_template, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

from models import Question, House, Answer


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/pt_db'
db = SQLAlchemy(app)

app.secret_key = os.urandom(50)


@app.route('/start', methods=['GET', 'POST'])
def get_user_name():
    if 'user' in session:
        return redirect('/end_test')
    if request.method == 'GET':
        return render_template('user_name_form.html')
    else:
        session['user'] = request.form['user_name']
        return render_template(
            'welcome_user.html',
            user=session['user']
        )


@app.route('/test', methods=['GET', 'POST'])
def do_the_test():
    if request.method == 'GET':
        questions = Question.query.all()
        return render_template('test_form.html', questions=questions)
    else:
        answers = []



@app.route('/end_test')
def drop_session():
    session.pop('user', None)
    flash('What was your name again...?')
    return redirect('/start')


if __name__ == '__main__':
    app.run(debug=True)