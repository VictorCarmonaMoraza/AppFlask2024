from flask import Flask, request, render_template, url_for, jsonify, session
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from Models.PersonaModel import Persona
from Database.database import db

app = Flask(__name__)
Bootstrap(app)

#Configuracion de la BD
USER_DB = 'postgres'
PASS_DB = 'Vcarmona32'
URL_DB = 'localhost'
NAME_DB = 'APPFLASK_DB'
FULL_URL_DB =f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

#Inicializacion del objeto db de sqlalchemy. Instancioamos objeto
##db = SQLAlchemy(app)  -->Esto propvoca despues de la refactorizacion referencia circular por lo cual
## debemos de sacarlo de esta forma y ponerlo de la forma que tenemos en la siguiente linea.
db.init_app(app)


##Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app,db)

##configuracion de flask-wtf
app.config['SECRET_KEY']='llave_secreta'






app.secret_key ='Mi_llave_secreta'


@app.route('/persona')
@app.route('/index')
@app.route('/index.html')
def crearPersona():
    ##Listado de personas. Nos devolvera todos los objeto persona de nuestra base de datos
    personasBD = Persona.query.all()
    total_personasBD = Persona.query.count()
    app.logger.debug(f'Listado Personas:{personasBD}')
    app.logger.debug(f'Total Personas:{total_personasBD}')
    return render_template('index.html',personasTemplate =personasBD, total_personasTemplate = total_personasBD)

@app.route('/agregar', methods=['GET','POST'])
def agregar_persona():
    #Primero debemos mostrar el formulario
    #Creamos un objeto de tipo Persona
    persona = Persona()

    return  render_template('detalle.html')


@app.route('/ver/<int:id>')
def ver_detalle(id):
    #Recuperamos la persona segun el id proporcionado
    #persona = Persona.query.get(id)
    personaBD = Persona.query.get_or_404(id)
    app.logger.debug((f'Ver persona: {personaBD}'))
    return render_template('detalle.html', personaTemplate = personaBD)

'''http://localhost:5000/'''
@app.route('/')
def inicio():
    if 'username' in session:
        app.logger.info(f'Hemos entrado al path {request.path}')
        return f'El usuario ha hecho login: {session["username"]}'
    return 'No ha hecho login'

@app.route('/login', methods=['GET','POST'])
def login():
    ##Diferenciar si es una peticionde tipo GET o de tipo POST
    if request.method == 'POST':
        ##Omitimos validaciones de usuario y password
        ##Rescatamos del formulario el usuario
        usuario = request.form['username']
        #Agregamos usuario a session
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

##salir de la session
@app.route('/logout')
def logout():
    ##Eliminamos de la session el usuario
    session.pop('username')
    ##Redireccionamos el metodo de inicio
    return redirect(url_for('inicio'))


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
    return redirect(url_for('inicio'))

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

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html',error = error),404

@app.route('/api/mostrar/<nombre>')
def mostrar_json(nombre):
    valores ={
        'nombre': nombre
    }
    return valores

@app.route('/api/mostrar2/<nombre>')
def mostrar_json2(nombre):
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    ##Transforma cualquier respuesta en un diccionario
    return jsonify(fruits)

@app.route('/api/mostrar3/<nombre>', methods=['GET','POST'])
def mostrar_json3(nombre):
    valores ={
        'nombre': nombre,
        'metodo_http': request.method
    }
    return valores