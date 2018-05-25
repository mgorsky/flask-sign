from flask import render_template, flash, redirect, url_for
from flask_mail import Message
from threading import Thread
from app import app, db, mail
from app.models import Signature
from app.forms import SignForm
from app.security import ts

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    signatures = Signature.query.order_by(Signature.timestamp.desc()).filter_by(verified=True)
    form = SignForm()
    if form.validate_on_submit():
        signature = Signature(first_name = form.first_name.data,
                              second_name = form.second_name.data,
                              affiliation = form.affiliation.data,
                              email = form.email.data,)
        if Signature.query.filter_by(email=signature.email).first() is not None:
          flash("""This email address is already in the database. Please check your inbox!.""",)
          return redirect(url_for('index'))
        db.session.add(signature)
        db.session.commit()
        flash("""Thank you for your signature! We've sent the confirmation email to: {}""".format(signature.email))
        recipient = signature.email
        token = ts.dumps(recipient, salt='email-confirm-key')
        confirm_url = url_for('confirm_email', token=token, _external=True)
        mess = Message("Weryfikacja podpisu", sender=("O prawo do milczenia", ""), recipients=[recipient,])
        mess.html = render_template('mail-confirm.html', confirm_url=confirm_url)
        Thread(target=mail.send(mess)).start()
        return redirect(url_for('index'))
    return render_template('merged.html', title='Merged!', form=form, signatures=signatures)

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt="email-confirm-key", max_age=604800)
    except:
        abort(404)
    signature = Signature.query.filter_by(email=email).first_or_404()

    signature.verified = True

    db.session.commit()

    return redirect(url_for('index'))