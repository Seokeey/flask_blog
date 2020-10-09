from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegisterationForm(FlaskForm):
    username = StringField(
        '아이디',
        validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField(
        '이메일',
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        '비밀번호', validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        '비밀번호 재확인', validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('회원가입')

 
class LoginForm(FlaskForm):
    email = StringField(
        '이메일',
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        '비밀번호', validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        '비밀번호 재확인', validators=[DataRequired(), EqualTo('password')]
    )

    remember = BooleanField('로그인 정보 저장')
    submit = SubmitField('로그인')
    
   