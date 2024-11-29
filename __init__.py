from flask import Flask
from flask_jwt_extended import JWTManager
from app.models.user import db, bcrypt
from app.routes import auth_bp, user_bp

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miapp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'clave-secreta'

    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)

    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api')

    return app
