from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import Usuario, db

def registro():
    """
    Controlador para registrar un nuevo usuario.
    """
    data = request.get_json()

    if not all(key in data for key in ("nombre", "email", "password")):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    if Usuario.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "El email ya está registrado"}), 400

    try:
        nuevo_usuario = Usuario(
            nombre=data["nombre"],
            email=data["email"],
            password_hash=Usuario.generar_password_hash(data["password"])
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def login():
    """
    Controlador para autenticar a un usuario.
    """
    data = request.get_json()

    if not all(key in data for key in ("email", "password")):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    usuario = Usuario.query.filter_by(email=data["email"]).first()
    if not usuario or not usuario.verificar_password(data["password"]):
        return jsonify({"error": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=usuario.id)
    return jsonify({"access_token": access_token}), 200
