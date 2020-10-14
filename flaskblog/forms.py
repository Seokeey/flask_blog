from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
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
        '비밀번호 재확인', validators=[
            DataRequired(),
            EqualTo(fieldname='password', message='비밀번호가 일치하지 않습니다.'),
            Length(min=8, 
                   max=20,
                   message='비밀번호는 최소 8글자 최대 20글자 이내로 입력해 주세요.'),
        ]
    )

    submit = SubmitField('회원가입')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('이미 사용중인 아이디 입니다.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('이미 사용중인 이메일 입니다.')


 
class LoginForm(FlaskForm):
    email = StringField(
        '이메일',
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        '비밀번호', validators=[DataRequired()]
    )

    remember = BooleanField('로그인 정보 저장')
    submit = SubmitField('로그인')

