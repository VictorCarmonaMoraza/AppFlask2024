from flask import Flask, request

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