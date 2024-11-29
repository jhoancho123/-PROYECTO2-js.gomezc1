from flask import Blueprint
from app.controllers.auth_controller import registro, login
from app.controllers.user_controller import obtener_usuario

# Crear Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)
auth_bp.add_url_rule('/auth/registro', 'registro', registro, methods=['POST'])
auth_bp.add_url_rule('/auth/login', 'login', login, methods=['POST'])

# Crear Blueprint para las rutas de usuario
user_bp = Blueprint('user', __name__)
user_bp.add_url_rule('/usuario', 'obtener_usuario', obtener_usuario, methods=['GET'])
