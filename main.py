#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import copy_current_request_context

from flask_mail import Mail
from flask_mail import Message

import threading

import forms
import model

app = Flask(__name__)

##https://support.google.com/accounts/answer/6010255?hl=en
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "eduardo@codigofacilito.com"
app.config['MAIL_PASSWORD'] = "C=eQ9KF="


mail = Mail(app)

def send_email(user):
	msg = Message("Test numero uno",
							sender="eduardo@codigofacilito.com",
							recipients=["eduardo78d@gmail.com"])
	msg.html = render_template('thanks.html', user = user)
	mail.send(msg)

@app.before_request
def before_request():
	g.db = model.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response

@app.route('/', methods=['GET'])
def index():
	title = "Curso Flask"
	context = {
		'title': title,
	}
	return render_template('index.html', context = context)

@app.route('/about', methods=['GET'])
def about():
	title = "About"
	context = {
		'title': title,
	}
	return render_template('about.html', context = context)

@app.route('/reviews', methods=['GET'])
@app.route('/reviews/<int:page>', methods=['GET'])
def review(page=1):
	paginate_by = 10
	next_page = 0

	title = "About"
	context = {
		'title': title,
	}
	#comments = model.Comment.select().limit(5).order_by(model.Comment.created_date.desc())
	comments = model.Comment.select().paginate(page, paginate_by).order_by(model.Comment.id.desc())
	if len(comments):
		last_id = comments[::-1][0].id
		if model.Comment.select().where(model.Comment.id < last_id).count():
			next_page = page + 1
	return render_template('review.html', context = context, comments = comments, next_page = next_page)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	title = "Contactanos"
	label = "¿Alguna pregunta o sugerencia?"

	@copy_current_request_context
	def send_message(message):
			send_email(message)

	form = forms.CommentForm(request.form)
	if request.method == 'POST' and form.validate():
		model.Comment.create(username = form.username.data,
												email = form.email.data,
												text = form.comment.data)

		flash('Tu comentario ha sido creado exitosamente!')
		sender = threading.Thread(name='mail_sender', target=send_message, args=("Thread",))
		sender.start()

		return redirect(url_for('review'))

	context = {
		'title': title,
		'label' : label
	}
	return render_template('contact.html', context = context, form = form)

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.run(debug=True, port=8000)


