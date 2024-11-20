from flask import Blueprint
from controllers import insertar_ingrediente_controller

ingredientes_bp = Blueprint('ingredientes', __name__)

@ingredientes_bp.route('/ingredientes', methods=['POST'])
def insertar_ingrediente():
    return insertar_ingrediente_controller()
