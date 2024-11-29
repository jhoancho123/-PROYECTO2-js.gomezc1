from flask import Blueprint, request, render_template
from app.controllers.auth_controller import autenticar_usuario, registrar_usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response, status_code = autenticar_usuario(data['username'], data['password'])
        return response, status_code
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response, status_code = registrar_usuario(data['username'], data['password'])
        return response, status_code
    return render_template('register.html')
