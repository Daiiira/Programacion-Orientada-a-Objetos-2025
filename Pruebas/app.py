# request sirve para enviar datos del cliente al servidor encapsulados en un objeto request global
#El objeto request posee el atributo method que permite saber el tipo de petición que hace el
#cliente (GET o POST). Es posible hacer el siguiente análisis: 
#if request.method == 'POST': 
#route() tambien puede recibir como parametro POST o GET para definir el tipo de petición que se espera en la ruta
#------------------------------------------------------------#

from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'CLAVE_SECRETA'

# secret key es necesaria para usar sesiones en Flask,
# se utiliza para firmar cookies y proteger datos de sesión
@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get["name"]
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

#------------------------------------------------------------#


@app.route('/')
def usuario():
    return render_template('nuevo_usuario.html')

@app.route('/bienvenida',methods = ['POST', 'GET'])
def bienvenida():
    if request.method == 'POST':
        if request.form['nombre'] and request.form['email'] and request.form['password']:
            datosf = request.form
            return render_template('bienvenida.html', datos=datosf, hora = datetime.now().hour)
        else:
            return render_template('nuevo_usuario.html')

def cargaTrabajador():
    pass

if __name__ == '__main__':
 app.run(debug = True)

#-----------------------------------#
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'

# Models
from flask import Flask, render_template#, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
#import os
import config

app = Flask(__name__)

db = SQLAlchemy(app)

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def inicio():
#    return render_template('index.html')
