from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)

    # Relación inversa
    productos = db.relationship('Producto', secondary='producto_ingrediente', back_populates='ingredientes')

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # 'Copa' o 'Malteada'
    
    # Relación con Ingredientes
    ingredientes = db.relationship('Ingrediente', secondary='producto_ingrediente', back_populates='productos')

class ProductoIngrediente(db.Model):
    __tablename__ = 'producto_ingrediente'
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)

# Cargar los ingredientes desde la base de datos
def cargar_ingredientes():
    ingredientes_db = Ingrediente.query.all()  # Trae todos los ingredientes de la base de datos
    ingredientes = []  # Lista que guardará las instancias de Ingrediente del modelo de mundo

    # Mapeamos cada ingrediente de la base de datos a un objeto de la clase Ingrediente
    for ingrediente_db in ingredientes_db:
        ingrediente = Ingrediente(
            nombre=ingrediente_db.nombre,
            precio=ingrediente_db.precio,
            calorias=ingrediente_db.calorias,
            inventario=ingrediente_db.inventario,
            es_vegetariano=ingrediente_db.es_vegetariano
        )
        ingredientes.append(ingrediente)
    
    return ingredientes


# Cargar los productos desde la base de datos
def cargar_productos():
    productos_db = Producto.query.all()  # Trae todos los productos de la base de datos
    productos = []  # Lista que guardará las instancias de Producto del modelo de mundo

    # Mapeamos cada producto de la base de datos a un objeto de la clase Producto
    for producto_db in productos_db:
        # Traer los ingredientes asociados a este producto
        ingredientes = cargar_ingredientes_por_producto(producto_db.id)

        # Creamos una instancia del producto en el modelo de mundo
        producto = Producto(
            nombre=producto_db.nombre,
            precio_publico=producto_db.precio_publico,
            ingredientes=ingredientes,  # Asignamos los ingredientes al producto
            tipo=producto_db.tipo
        )
        productos.append(producto)

    return productos


# Función auxiliar para cargar los ingredientes de un producto
def cargar_ingredientes_por_producto(producto_id):
    ingredientes_db = Ingrediente.query.join(ProductoIngrediente).filter(ProductoIngrediente.producto_id == producto_id).all()
    ingredientes = []
    
    for ingrediente_db in ingredientes_db:
        ingrediente = Ingrediente(
            nombre=ingrediente_db.nombre,
            precio=ingrediente_db.precio,
            calorias=ingrediente_db.calorias,
            inventario=ingrediente_db.inventario,
            es_vegetariano=ingrediente_db.es_vegetariano
        )
        ingredientes.append(ingrediente)

    return ingredientes
