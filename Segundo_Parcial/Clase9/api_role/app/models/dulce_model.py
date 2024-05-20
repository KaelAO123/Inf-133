from database import db


# Define la clase `Dulce` que hereda de `db.Model`
# `Dulce` representa la tabla `librs` en la base de datos
class Dulce(db.Model):
    __tablename__ = "dulces"

    # Define las columnas de la tabla `librs`
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    sabor = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.Float(),nullable=False)

    # Inicializa la clase `Dulce`
    def __init__(self, marca, sabor, origen,peso):
        self.marca = marca
        self.sabor = sabor
        self.origen = origen
        self.peso = peso

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Dulce.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Dulce.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, marca=None, sabor=None, origen=None, peso=None):
        if marca is not None:
            self.marca = marca
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        if peso is not None:
            self.peso = peso
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
