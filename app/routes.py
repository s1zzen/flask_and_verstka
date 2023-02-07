from app import app, db
from app.forms import ApplicationForm
from app.models import Application
from flask import render_template, flash, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(username=form.username.data,
                                  body=form.body.data, phone=form.phone.data)
        db.session.add(application)
        db.session.commit()
        flash('Congratulations')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
