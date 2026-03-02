from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/MyWeb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Skill(db.Model):
    __tablename__ = 'skills'
    __table_args__ = {'schema':'Portfolio'}

    id = db.Column(db.Integer, primary_key = True)
    skill_name = db.Column(db.String(255))

    def __init__(self, skill_name):
        self.skill_name = skill_name


@app.route('/home')
def home():
        my_skill = Skill.query.all()
        return render_template('index.html', skills = my_skill)
@app.route('/skill')
def skill():
        return render_template('skill.html')

if __name__ == '__main__':
    app.run(debug=True)
