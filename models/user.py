from app import db, bcrypt

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.generar_password_hash(password)

    @staticmethod
    def generar_password_hash(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verificar_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @classmethod
    def autenticar(cls, username, password):
        usuario = cls.query.filter_by(username=username).first()
        if usuario and usuario.verificar_password(password):
            return usuario
        return None
