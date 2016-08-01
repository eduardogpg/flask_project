from flask import Flask
from flask import request
from flask import flash
from flask import redirect
from flask import render_template

from aux import CommentForm

class Comment:
	def __init__(self, username, email, comment):
		self.username = username
		self.email = email
		self.comment = comment

	def get_username(self):
		return self.username

	def get_email(self):
		return self.email

	def get_comment(self):
		return self.comment

listComments = []
app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route('/', methods=['GET'])
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

@app.route('/comentario',methods=['GET', 'POST'])
def comment():
  form = CommentForm(request.form)
  if request.method == 'POST' and form.validate():
  	listComments.append( Comment(form.username.data, form.email.data, form.comment.data) )
  	flash('Gracias por enviar tu comentario ' + str( len(listComments) ) )

  return render_template('comment.html', form=form )

if __name__ == '__main__':
	app.run()


