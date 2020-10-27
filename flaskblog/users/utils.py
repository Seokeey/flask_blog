import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

    
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('비밀번호 재설정하기',
                  sender='noreply@demo.com', 
                  recipients=[user.email])
    msg.body = f'''비밀번호를 재설정하기 위해 다음의 링크를 방문해주세요:
    {url_for('reset_token', token=token, _external=True)} 
    만약 비밀번호 재설정하기를 하신적이 없는 경우 뒤로가기를 눌러주세요.
    '''
    mail.send(msg)