from flask import Flask
app = Flask(__name__)

@app.route("/hello/world")
def hello_world():
	return '<h2> Hello world </h2>'

@app.route("/user/<name>")
def user(name):
	return '<h2> Hello ' + name + '</h2>'	

#http://stackoverflow.com/questions/19574694/flask-hit-decorator-before-before-request-signal-fires
@app.before_request
def before_request():
	print "Hola mundo"

def index():
	return 'index dos:3'	

if __name__ == '__main__':
	app.add_url_rule('/', 'index', index)
	app.run()