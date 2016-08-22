from wtforms import Form, TextAreaField, StringField, PasswordField, validators, TextField
from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    username = StringField('Username', 
    						[validators.Length(min=4, max=25, message='Ingrese un username valido')], 
    						render_kw={"placeholder": "Username"} )

    email = EmailField('Correo Electronico',
    					[ validators.Email( message='Ingrese correo electronico valido')],
    					render_kw={"placeholder": "Email"} )

    comment = TextAreaField('Comentario', [validators.Length(min=5, max=255, 
    					message ='El comentario debe contener por lo menos 5 caracteres')],
    					render_kw={"placeholder": "Comentario"} )
