from flask import Blueprint, request, jsonify
from models.libro_model import Libro
from views.libro_view import render_libro_list, render_libro_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

# Crear un blueprint para el controlador de animales
libro_bp = Blueprint("libro", __name__)


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper


# Ruta para obtener la lista de animales
@libro_bp.route("/libros", methods=["GET"])
@jwt_required
def get_animals():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))


# Ruta para obtener un libro específico por su ID
@libro_bp.route("/libros/<int:id>", methods=["GET"])
@jwt_required
def get_animal(id):
    libro = Libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "Libro no encontrado"}), 404


# Ruta para crear un nuevo libro
@libro_bp.route("/libros", methods=["POST"])
@jwt_required
def create_animal():
    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Validación simple de datos de entrada
    if disponibilidad is None or not titulo or not autor or edicion is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo libro y guardarlo en la base de datos
    libro = Libro(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)
    libro.save()

    return jsonify(render_libro_detail(libro)), 201


# Ruta para actualizar un libro existente
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
@jwt_required
def update_animal(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Actualizar los datos del libro
    libro.update(titulo=titulo, autor=autor, edicion=edicion,disponibilidad=disponibilidad)

    return jsonify(render_libro_detail(libro))


# Ruta para eliminar un libro existente
@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
@jwt_required
def delete_animal(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    # Eliminar el libro de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
