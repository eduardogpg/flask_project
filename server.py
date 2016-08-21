from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	title = "Resort Facilito"
	context = {
		'title': title,
	}

	return render_template('index.html', context = context)

if __name__ == '__main__':
	app.run(debug=True, port=8000)


