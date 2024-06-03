from flask import Blueprint, request, jsonify
from app.models.product_model import Product
from app.views.product_view import render_product_detail, render_products
from flask_jwt_extended import verify_jwt_in_request
from utils.decorators import jwt_required, roles_required

product_bp = Blueprint("product",__name__)

@product_bp.route("/products",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_product():
    products = Product.get_all()
    return render_products(products)

@product_bp.route("/products/<int: id>",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_product(id):
    product = Product.get_by_id(id)
    return render_product_detail(product)

@product_bp.route("/products",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_product():
    data = request.json
    name = data["name"]
    description = data["description"]
    price = data["price"]
    stock = data["stock"]

    if not name or not description or price is None or stock is None:
        return jsonify({"error":"Faltan requerimientos"}),400
    
    product = Product(name=name,description=description,price=price,stock=stock)
    product.save()
    return jsonify(render_product_detail(product)),201

@product_bp.route("/products/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_product(id):
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error":"Producto no encontrado"}),404
    
    data = request.json
    name = data["name"]
    description = data["description"]
    price = data["price"]
    stock = data["stock"]
    product.update(name=name,description=description,price=price,stock=stock)
    return jsonify(render_product_detail(product)),201

@product_bp.route("/products/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_product(id):
    product = Product.get_by_id(id)
    if not product:
        return jsonify({"error":"El producto no existe"}),404
    product.delete()
    return "",204
