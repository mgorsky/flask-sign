from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from .models import Signature
import sqlite3

class EmailForm(FlaskForm):
    email = StringField("Adres e-mail", validators=[DataRequired(message="Pole nie może być puste!"), 
                                                            Email(message="Nieprawidłowy adres e-mail!")])
    submit = SubmitField("Wyślij wiadomość!")


class SignForm(FlaskForm):
    first_name = StringField('Imię', validators=[DataRequired(message='Imię nie może być puste!')])
    second_name = StringField('Nazwisko', validators=[DataRequired(message='Nazwisko nie może być puste!')])
    affiliation = StringField()
    email = StringField('Adres e-mail', validators=[DataRequired(message='E-mail nie może być pusty!'), 
                                                    Email(message='Nieprawidłowy adres e-mail!')])
    submit = SubmitField('Podpisz list!')