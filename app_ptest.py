from flask import Flask, request, render_template, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

from models import Question, House, Answer


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/pt_db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
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
        questions = Question.query.all()
        quest_ids = [question.id for question in questions]
        answers_value = []
        for question in quest_ids:
            val = request.form['answer-option{}' .format(question)]
            answers_value.append(val)
        gryffindor_result = {'id_house': 1, 'score': len([val for val in answers_value if val == 1])}
        hafflepuff_result = {'id_house': 4, 'score': len([val for val in answers_value if val == 4])}
        slytherin_result = {'id_house': 2, 'score': len([val for val in answers_value if val == 2])}
        ravenclaw_result = {'id_house': 3, 'score': len([val for val in answers_value if val == 3])}
        all_results = [gryffindor_result, hafflepuff_result, slytherin_result, ravenclaw_result]
        highest_score = [all_results[0]]
        for result in all_results:
            if result['score'] > highest_score[0]['score']:
                highest_score.pop()
                highest_score.append(result)
        selected_house = House.query.get(highest_score[0]['id_house'])
        return 'not finished  but House id is {}' .format(highest_score[0]['id_house'])







@app.route('/end_test')
def drop_session():
    session.pop('user', None)
    flash('What was your name again...?')
    return redirect('/start')


if __name__ == '__main__':
    app.run(debug=True)