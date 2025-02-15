from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_list, render_dulce_detail
from utils.decorators import jwt_required, roles_required

# Crear un blueprint para el controlador de libroes
dulce_bp = Blueprint("dulce", __name__)


# Ruta para obtener la lista de libroes
@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libros():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces))


# Ruta para obtener un dulce específico por su ID
@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_libro(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "Dulce no encontrado"}), 404


# Ruta para crear un nuevo dulce
@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_libro():
    data = request.json
    marca = data.get("marca")
    sabor = data.get("sabor")
    peso = data.get("peso")
    origen = data.get("origen")

    # Validación simple de datos de entrada
    if origen is None or not marca or not sabor or peso is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo dulce y guardarlo en la base de datos
    dulce = Dulce(marca=marca, sabor=sabor, peso=peso, origen=origen)
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201


# Ruta para actualizar un dulce existente
@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_libro(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "Dulce no encontrado"}), 404

    data = request.json
    marca = data.get("marca")
    sabor = data.get("sabor")
    peso = data.get("peso")
    origen = data.get("origen")

    # Actualizar los datos del dulce
    dulce.update(marca=marca, sabor=sabor, peso=peso,origen=origen)

    return jsonify(render_dulce_detail(dulce))



# Ruta para eliminar un dulce existente
@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_libro(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "Dulce no encontrado"}), 404

    # Eliminar el dulce de la base de datos
    dulce.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
