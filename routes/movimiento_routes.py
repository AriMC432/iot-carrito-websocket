from flask import Blueprint
from controllers.movimiento_controller import MovimientoController

movimiento_routes = Blueprint(
    "movimiento_routes",
    __name__
)

# =========================================
# AGREGAR MOVIMIENTO
# =========================================
movimiento_routes.route(
    "/api/movimiento",
    methods=["POST"]
)(MovimientoController.agregar_movimiento)


# =========================================
# ULTIMO MOVIMIENTO
# =========================================
movimiento_routes.route(
    "/api/ultimo_movimiento",
    methods=["GET"]
)(MovimientoController.ultimo_movimiento)


# =========================================
# ACTUALIZAR MOTOR
# =========================================
movimiento_routes.route(
    "/api/actualizar_motor",
    methods=["PUT"]
)(MovimientoController.actualizar_motor)


# =========================================
# VER CONFIG MOTOR
# =========================================
movimiento_routes.route(
    "/api/ver_config_motor/<int:id_movimiento>",
    methods=["GET"]
)(MovimientoController.ver_config_motor)