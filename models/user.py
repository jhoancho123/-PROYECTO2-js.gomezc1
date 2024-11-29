from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def verificar_password(self, password):
        """
        Verifica si el password proporcionado coincide con el hash almacenado.
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def generar_password_hash(password):
        """
        Genera un hash a partir de un password plano.
        """
        return bcrypt.generate_password_hash(password).decode('utf-8')
