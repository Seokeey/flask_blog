from flask import render_template, redirect, url_for, flash
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



posts = [
    {
        'author': 'JoonSeok Lee',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 7, 2020',
    },
    {
        'author': 'JoonSeok Lee',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 8, 2020',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='소개')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"{form.username.data}로 계정이 생성되어 로그인이 가능합니다.", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title='회원가입', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('이메일 또는 비밀번호를 다시 확인해주세요.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
