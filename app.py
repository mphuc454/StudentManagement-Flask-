from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'Hello'
app.permanent_session_lifetime = timedelta(minutes=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/MyWeb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Skill(db.Model):
    __tablename__ = 'skills'
    __table_args__ = {'schema':'Portfolio'}

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


@app.route('/home')
def home():
        my_skill = Skill.query.all()
        return render_template('index.html', skills = my_skill)
@app.route('/skill')
def skill():
        return render_template('skill.html')
@app.route('/demo', methods = ['GET','POST'])
def demo():
    if request.method == 'POST':
        session.permanent = True
        useremail = request.form['email']
        session['email'] = useremail
        return redirect(url_for('usr'))
    else:
        return render_template('demo.html')

@app.route('/user')
def usr():
    if 'email' in session:
        usremail = session['email']
        return f"<h1>{usremail}</h1>"
    else:
        return redirect(url_for('demo'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    return  redirect(url_for('demo'))
if __name__ == '__main__':
    app.run(debug=True)
