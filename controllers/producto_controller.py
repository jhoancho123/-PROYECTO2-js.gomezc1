from flask import request, jsonify
from models import Producto, db
from utils.responses import not_found, bad_request, success

def consultar_todos_productos():
    productos = Producto.query.all()
    return jsonify([{
        "id": producto.id,
        "nombre": producto.nombre,
        "precio_publico": producto.precio_publico,
        "tipo": producto.tipo,
        "inventario": producto.inventario
    }])

def consultar_producto_por_id(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return not_found("Producto no encontrado.")
    return jsonify({
        "id": producto.id,
        "nombre": producto.nombre,
        "precio_publico": producto.precio_publico,
        "tipo": producto.tipo,
        "inventario": producto.inventario
    })

def consultar_producto_por_nombre(nombre):
    producto = Producto.query.filter_by(nombre=nombre).first()
    if not producto:
        return not_found("Producto no encontrado.")
    return jsonify({
        "id": producto.id,
        "nombre": producto.nombre,
        "precio_publico": producto.precio_publico,
        "tipo": producto.tipo,
        "inventario": producto.inventario
    })

def consultar_calorias_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto:
        return not_found("Producto no encontrado.")
    ingredientes = producto.ingredientes  # Asumimos relación con ingredientes
    total_calorias = sum([ing.calorias for ing in ingredientes])
    return jsonify({"calorias_totales": total_calorias})

def vender_producto(producto_id):
    producto = Producto.query.get(producto_id)
    if not producto or producto.inventario <= 0:
        return not_found("Producto no disponible.")
    producto.inventario -= 1
    db.session.commit()
    return success(f"Producto '{producto.nombre}' vendido exitosamente.")

def reabastecer_producto(producto_id, cantidad):
    producto = Producto.query.get(producto_id)
    if not producto:
        return not_found("Producto no encontrado.")
    producto.inventario += cantidad
    db.session.commit()
    return success(f"Inventario del producto '{producto.nombre}' actualizado.")
