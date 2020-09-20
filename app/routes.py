from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    user = {'username' : 'Anjay Partha'}
    courses = [{'name': 'Basic I', 'duration' : '5 weeks'}, {'name' : 'Ashtakam I', 'duration' : '3 weeks'}]
    return render_template('/index.html', user=user,courses=courses)


@app.route('/login', methods=["GET", "POST"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        flash('login requested for user {} with remember me {}'.format(login.username.data, login.remember_me.data))
        return redirect(url_for('index'))
    return render_template('/login.html', form=login)



@app.route('/help')
def help():
    return render_template('help.html')