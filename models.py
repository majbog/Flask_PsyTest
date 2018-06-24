from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    quest = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

    def __init__(self, text, quest, house_id,):

        self.text = text
        self.quest = quest
        # self.house = house
        self.house_id = house_id


if __name__ == '__main__':
    # db.create_all()
    # print('created tables')
    # gryffindor = House('Gryffindor', 'sample description1')
    # hufflepuff = House('Hufflepuff', 'sample description2')
    # ravenclaw = House('Ravenclaw', 'sample description3')
    # slytherin = House('Slytherin', 'sample description4')
    # db.session.add(gryffindor)
    # db.session.add(hufflepuff)
    # db.session.add(ravenclaw)
    # db.session.add(slytherin)
    # db.session.commit()
    # print(gryffindor.id)
    q1 = Question('sample question1')
    a1 = Answer('sample answer1', 1, 1)
    db.session.add(q1)
    db.session.add(a1)
    db.session.commit()
    print(a1.id)

