#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from aux import CommentForm

app = Flask(__name__)

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
	return render_template('review.html', context = context)

@app.route('/contact', methods=['GET'])
def contact():
	title = "Contactanos"
	label = "¿Alguna pregunta o sugerencia?"

	form = CommentForm()

	context = {
		'title': title,
		'label' : label
	}

	return render_template('contact.html', context = context, form = form)

if __name__ == '__main__':
	app.run(debug=True, port=8000)


