from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from data_test import questions, answers, houses

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/pt_db'
db = SQLAlchemy(app)


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    rel_answers = db.relationship('Answer', backref='house', uselist=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    answers = db.relationship('Answer', backref='question', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, text):
        self.text = text
        # self.answers = answers


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

    def __init__(self, text, question_id, house_id,):

        self.text = text
        self.question_id = question_id
        # self.house = house
        self.house_id = house_id


if __name__ == '__main__':
    db.create_all()
    print('created tables')
    # pupulate database
    for key in houses:
        h = House(key, houses[key])
        db.session.add(h)
    for q in questions:
        db.session.add(q)
    for answer in answers:
        a = Answer(answer[0], answer[1], answer[2])
        db.session.add(a)
    db.session.commit()


