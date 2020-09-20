from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SubscribeForm
from flask import request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Subscriber

@app.route('/')
@app.route('/index', methods=["GET"])
def index():
    subscribe = SubscribeForm()
    return render_template('/index.html', form=subscribe)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login = LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(username=login.username.data).first()
        print ('user password is {} and stored hash is {}'.format(login.password.data, user.password_hash))
        if user is None or not user.check_password(login.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=login.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    else:
        return render_template('login.html', form=login)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/subscribe', methods=['POST'])
def subscribe():
    subscribe = SubscribeForm()
    sub = Subscriber()
    sub.email = subscribe.email_id.data
    db.session().add(sub)
    db.session().commit()
    return redirect('index')