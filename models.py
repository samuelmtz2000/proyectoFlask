from flask_sqlalchemy import SQLAlchemy
# from app import app
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    contrasenia = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    nombre = db.Column(db.String(100))

    def __init__(self, username="", contrasenia="", correo="", nombre=""):
        self.username = username,
        self.contrasenia = contrasenia
        self.correo = correo
        self.nombre = nombre

    # def __repr__(self):
    #     return '<User %r>' % self.username
