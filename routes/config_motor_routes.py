from flask import Blueprint
from flask import request

from models.movimiento_model import MovimientoModel

config_motor_routes = Blueprint(
    "config_motor_routes",
    __name__
)

# =========================================
# VER CONFIG MOTOR
# =========================================

@config_motor_routes.route(
    "/api/config_motor/<id_movimiento>",
    methods=["GET"]
)
def ver_config_motor(id_movimiento):

    response = MovimientoModel.ver_config_motor(
        id_movimiento
    )

    return response


# =========================================
# ACTUALIZAR CONFIG
# =========================================

@config_motor_routes.route(
    "/api/config_motor",
    methods=["POST"]
)
def actualizar_config():

    data = request.json

    response = MovimientoModel.actualizar_config_motor(

        data["id_movimiento"],

        data["MIA"],
        data["MIB"],
        data["MITime"],

        data["MDA"],
        data["MDB"],
        data["MDTime"]

    )

    return response