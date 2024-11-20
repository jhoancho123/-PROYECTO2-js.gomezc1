from flask import request, jsonify
from models import Ingrediente

def insertar_ingrediente_controller():
    """
    Controlador para manejar la inserción de ingredientes.
    """
    data = request.get_json()  # Suponiendo que se recibe un JSON
    try:
        nuevo_ingrediente = Ingrediente.insertar_ingrediente(
            nombre=data['nombre'],
            precio=data['precio'],
            calorias=data['calorias'],
            inventario=data['inventario'],
            es_vegetariano=data['es_vegetariano']
        )
        return jsonify({
            "message": "Ingrediente creado exitosamente",
            "ingrediente": {
                "id": nuevo_ingrediente.id,
                "nombre": nuevo_ingrediente.nombre
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
