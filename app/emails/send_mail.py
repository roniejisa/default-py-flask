from flask_mail import Message
from flask import render_template
from ..extensions import mail

def send_welcome_email(to, username):
    msg = Message('Welcome!', sender='noreply@yourapp.com', recipients=[to])
    msg.body = f'Hello {username}, welcome to our platform!'
    msg.html = render_template('emails/welcome.html', username=username)
    mail.send(msg)
