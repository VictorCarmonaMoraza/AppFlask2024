from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

'''http://localhost:5000/'''
@app.route('/')
def hello_world():
    app.logger.info(f'Hemos entrado al path {request.path}')
    return 'Hola Mundo desde Flask'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    app.logger.info(f'Hemos entrado al path {request.path}')
    return f'Saludos {nombre.upper()}'


@app.route('/edad/<int:edad>')
def edad(edad):
    app.logger.info(f'Hemos entrado al path {request.path}')
    return f'Tu edad es: {edad}'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return f'Tu nombre es {nombre}'

@app.route('/mostrar2/<nombre2>', methods=['GET','POST'])
def mostrar_nombre2(nombre2):
    return render_template('mostrar.html',nombre_llave =nombre2)

@app.route('/redireccionar')
def redireccionar():
    ##Redirecciona a otro metodo que es lo que ira en el url_for
    #Con url for le decimos el metodo que se va a ejecutar
    return redirect(url_for('hello_world'))

@app.route('/redireccionar2')
def redireccionar2():
    ##Redirecciona a otro metodo que es lo que ira en el url_for
    #Con url for le decimos el metodo que se va a ejecutar
    return redirect(url_for('mostrar_nombre', nombre = 'Victor'))


@app.route('/redireccionar3')
def redireccionar3():
    ##Redirecciona a otro metodo que es lo que ira en el url_for
    #Con url for le decimos el metodo que se va a ejecutar
    return render_template('mostrar.html', nombre_llave='Pedro')