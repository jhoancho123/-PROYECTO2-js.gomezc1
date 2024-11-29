from flask import request, jsonify, session
from models import user, db
from utils.responses import unauthorized, success, bad_request

def registrar_user():
    """
    Endpoint para registrar un nuevo user.
    """
    datos = request.get_json()
    username = datos.get('username')
    password = datos.get('password')
    es_admin = datos.get('es_admin', False)
    es_empleado = datos.get('es_empleado', False)

    if not username or not password:
        return bad_request("El nombre de user y la contraseña son obligatorios.")
    
    if user.query.filter_by(username=username).first():
        return bad_request("El nombre de user ya está en uso.")

    nuevo_user = user(username=username, password=password, es_admin=es_admin, es_empleado=es_empleado)
    db.session.add(nuevo_user)
    db.session.commit()

    return success(f"user '{username}' creado exitosamente.")

def autenticar_user():
    """
    Endpoint para autenticar un user.
    """
    datos = request.get_json()
    username = datos.get('username')
    password = datos.get('password')

    user = user.autenticar(username, password)
    if not user:
        return unauthorized("Nombre de user o contraseña incorrectos.")
    
    session['user_id'] = user.id
    session['es_admin'] = user.es_admin
    session['es_empleado'] = user.es_empleado

    return success(f"user '{username}' autenticado exitosamente.")
