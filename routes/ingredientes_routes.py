# app/routes/ingrediente_routes.py
from flask import Blueprint, request, jsonify
from controllers.heladeria_controller import obtener_ingredientes, crear_ingrediente

ingrediente_bp = Blueprint('ingredientes', __name__, url_prefix='/api/ingredientes')

@ingrediente_bp.route('/', methods=['GET'])
def listar_ingredientes():
    ingredientes = obtener_ingredientes()
    return jsonify([{
        'id': i.id,
        'nombre': i.nombre,
        'precio': i.precio,
        'calorias': i.calorias,
        'inventario': i.inventario,
        'es_vegetariano': i.es_vegetariano
    } for i in ingredientes])

@ingrediente_bp.route('/', methods=['POST'])
def nuevo_ingrediente():
    data = request.get_json()
    ingrediente = crear_ingrediente(data)
    return jsonify({
        'id': ingrediente.id,
        'nombre': ingrediente.nombre
    }), 201
