from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    es_admin = db.Column(db.Boolean, default=False, nullable=False)
    es_empleado = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, username, password, es_admin=False, es_empleado=False):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.es_admin = es_admin
        self.es_empleado = es_empleado

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def autenticar(username, password):
        usuario = Usuario.query.filter_by(username=username).first()
        if usuario and usuario.verificar_password(password):
            return usuario
        return None
