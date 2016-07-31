from flask import Flask
from flask import render_template

app = Flask(__name__)# template_folder='templates')

@app.route('/')
def index():
	title = "Resort Facilito"
	hotel_name = "Facilito Resort"
	num_available_room = 400;

	context = {
		'title': title,
		'hotel_name' : hotel_name,
		'num_available_room' : num_available_room
	}
	return render_template('index.html', context = context)

@app.route('/contact')
def contact():
	title = "Contacto Resort Facilito"
	hotel_name = "Facilito Resort"
	num_available_room = 400;

	context = {
		'title': title,
		'hotel_name' : hotel_name,
		'num_available_room' : num_available_room
	}
	return render_template('contact.html', context = context)

if __name__ == '__main__':
	app.run()