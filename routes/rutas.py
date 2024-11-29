from flask import Blueprint
from controladores.producto_controller import (
    consultar_todos_productos,
    consultar_producto_por_id,
    consultar_producto_por_nombre,
    consultar_calorias_producto,
    vender_producto,
    reabastecer_producto
)

rutas = Blueprint('rutas', __name__)

# Endpoints para productos
rutas.route('/productos', methods=['GET'])(consultar_todos_productos)
rutas.route('/productos/<int:producto_id>', methods=['GET'])(consultar_producto_por_id)
rutas.route('/productos/nombre/<string:nombre>', methods=['GET'])(consultar_producto_por_nombre)
rutas.route('/productos/<int:producto_id>/calorias', methods=['GET'])(consultar_calorias_producto)
rutas.route('/productos/<int:producto_id>/vender', methods=['POST'])(vender_producto)
rutas.route('/productos/<int:producto_id>/reabastecer', methods=['POST'])(reabastecer_producto)
