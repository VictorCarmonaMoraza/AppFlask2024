from Database.database import db


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    ##Obtrener una represetnacion de la clase
    def __str__(self):
        return (
            f'Id:{self.id}'
            f'Nombre:{self.nombre}'
            f'Apellido:{self.apellido}'
            f'Email:{self.email}'
        )