from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/pt_db'
db = SQLAlchemy(app)

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    answers = db.relationship('Answer', backref='answer', lazy=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    question = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    house = db.relationship('House', backref="answers")

    

if __name__ == '__main__':
    app.run(debug=True)