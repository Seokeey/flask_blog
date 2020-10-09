from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b9dba15492c53c6267f42d9ed3745e1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.integeer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"




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
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f"{form.username.data}로 계정이 생성됐습니다.", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='회원가입', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 관리자 계정 로그인
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('로그인 되었습니다!', 'success')
            return redirect(url_for('home'))

    return render_template('login.html', title='로그인', form=form)


if __name__ == "__main__":
    app.run(debug=True)

