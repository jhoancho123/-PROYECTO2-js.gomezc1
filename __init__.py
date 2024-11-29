from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Inicialización de extensiones
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miapp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'clave-secreta'
    
    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)

    # Registrar Blueprints
    from app.views.auth_views import auth_bp
    app.register_blueprint(auth_bp)

    return app
