#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

import forms
import model

app = Flask(__name__)

@app.before_request
def before_request():
	g.db = model.DATABASE
	g.db.connect()
	print "Conexión exitosa"

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
def review():
	title = "About"
	context = {
		'title': title,
	}
	comments = model.Comment.select().limit(5).order_by('created_date')
	return render_template('review.html', context = context, comments = comments)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	title = "Contactanos"
	label = "¿Alguna pregunta o sugerencia?"

	form = forms.CommentForm(request.form)
	if request.method == 'POST' and form.validate():
		model.Comment.create(username = form.username.data,
												email = form.email.data,
												text = form.comment.data)

		flash('Tu comentario ha sido creado exitosamente!')
		return redirect(url_for('review'))

	context = {
		'title': title,
		'label' : label
	}
	return render_template('contact.html', context = context, form = form)

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.run(debug=True, port=8000)


