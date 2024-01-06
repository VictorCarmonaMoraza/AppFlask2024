from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido')
    email = StringField('Email',validators=[DataRequired()])
    ##Botones que tendra en formulario
    enviar = SubmitField('Enviar')