from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm
# from models.UserInfo import UserInfo
# inicializar la app de flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretodeamor'

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

db = SQLAlchemy(app)


@app.route('/')
def index():

    return render_template("index.html", title="Esta es mi aplicación")


@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.form:
        print(request.form)
    return render_template("loginForm.html")


if __name__ == "__main__":
    app.run(debug=True)
