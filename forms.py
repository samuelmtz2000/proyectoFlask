from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired


class LoginForm(Form):
    usuario = StringField('Usuario', validators=[InputRequired()])
    contrasenia = PasswordField('Contraseña', validators=[InputRequired()])
    correo = EmailField('Correo', [
        validators.required(message='El apellido es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    nombre = StringField('Nombre', validators=[
        validators.required(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])

# id = db.Column(db.Integer, primary_key=True)
# username = db.Column(db.String(100), unique=True)
# contrasenia = db.Column(db.String(100))
# correo = db.Column(db.String(100))
# nombre = db.Column(db.String(100))
