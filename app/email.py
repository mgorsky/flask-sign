from flask import render_template
from flask_mail import Message
from app import app, mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender="weryfikacja@oprawodomilczenia.pl", recipients=recipients)
    msg.body = "text_body"
    msg.html = "html_body"
    # msg.body = text_body
    # msg.html = html_body
    mail.send(msg)


def send_confirmation_email(self, Signature):
    send_email('[O prawo do milczenia] Potwierdzenie podpisu',
               sender=app.config.MAIL_USERNAME, #zoba jak było w razie wyjebki na tej linii
               recipients=[Signature.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token='token'),
               html_body=render_template('email/mail-confirm.html',
                                         user=user, token='token'))