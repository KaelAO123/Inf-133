from database import db


# Define la clase `Dulce` que hereda de `db.Model`
# `Dulce` representa la tabla `dulces` en la base de datos
class Dulce(db.Model):
    __tablename__ = "dulces"

    # Define las columnas de la tabla `dulces`
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    sabor = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100),nullable=False)
    peso = db.Column(db.Float(), nullable=False)

    # Inicializa la clase `Dulce`
    def __init__(self, marca, sabor, peso, origen):
        self.marca = marca
        self.sabor = sabor
        self.peso = peso
        self.origen  = origen

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
    def update(self, marca=None, sabor=None, peso=None, origen=None):
        if marca is not None:
            self.marca = marca
        if sabor is not None:
            self.sabor = sabor
        if peso is not None:
            self.peso = peso
        if origen is not None:
            self.origen = origen
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
