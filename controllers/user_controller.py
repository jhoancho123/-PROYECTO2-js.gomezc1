from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import Usuario

@jwt_required()
def obtener_usuario():
    """
    Controlador para obtener los datos del usuario autenticado.
    """
    usuario_id = get_jwt_identity()
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify({
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email
    }), 200
