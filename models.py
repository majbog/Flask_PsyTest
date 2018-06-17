from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/pt_db'
db = SQLAlchemy(app)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, name, description):
        self.id = id
        self.name = name
        self.description = description



class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    answers = db.relationship('Answer', backref='answer', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, id, text, answers):
        self.id = id
        self.text = text
        self.answers = answers


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    question = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    house = db.relationship('House', uselist=False)

    def __init__(self, id, text, question, house, house_id):
        self.id = id
        self.text = text
        self.question = question
        self.house = house
        self.house_id = house_id


if __name__ == '__main__':
    db.create_all()
    print('created')
    app.run(debug=True)