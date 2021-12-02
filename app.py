from flask import Flask, render_template, flash, request, redirect, url_for
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import exists
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
import forms
from sqlalchemy import text
import models
# from models import db
from models import User, db
import win32api


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretodeamor'
app.config.from_object(DevelopmentConfig)
db.init_app(app)

csrf = CSRFProtect()


@app.route('/', methods=['GET', 'POST'])
def Login():
    create_form = forms.LoginForm()
    if request.form:
        us = request.form.get("usuario")
        contrasenia = request.form.get("contrasenia")
        user = db.session.query(User).filter(
            User.username == us).filter(User.contrasenia == contrasenia).first()
        if user is not None:
            return render_template("index.html", user=user)
    return render_template("loginForm.html", form=create_form)


@app.route("/registro", methods=['POST', "GET"])
def Register():
    create_form = forms.LoginForm()
    if request.form:
        correo = request.form.get("correo")
        contrasenia = request.form.get("contrasenia")
        nombre = request.form.get("nombre")
        usuario = request.form.get("usuario")
        userInfo = models.User(usuario, contrasenia, correo, nombre)
        print(correo, usuario, nombre, contrasenia, userInfo)
        try:
            db.session.add(userInfo)
            db.session.commit()
            return redirect("/")
        except:
            print("problema al insertar")
            win32api.MessageBox(0, 'Error al insertar', 'error')

    return(render_template("registerForm.html", form=create_form))


@app.route("/cerrar_session", methods=["POST", "GET"])
def CerrarSession():
    create_form = forms.LoginForm()
    return render_template("loginForm.html", form=create_form)


if __name__ == "__main__":
    # init_db()
    app.run(debug=True)
