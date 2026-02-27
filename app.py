
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login_usr():
    return render_template('login.html')
@app.route('/home')
def home():
        return render_template('index.html')
@app.route('/logout')
def logout():
    return redirect(url_for('login_usr'))

if __name__ == '__main__':
    app.run(debug=True)
