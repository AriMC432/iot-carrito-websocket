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
# =========================================
# CREAR DEMO
# =========================================

movimiento_routes.route(
    "/api/crear_demo",
    methods=["POST"]
)(MovimientoController.crear_demo)

# =========================================
# VER DEMOS
# =========================================

movimiento_routes.route(
    "/api/ver_demos",
    methods=["GET"]
)(MovimientoController.ver_demos)

# =========================================
# VER DETALLE DEMO
# =========================================

movimiento_routes.route(
    "/api/ver_demo_detalle/<int:id_demo>",
    methods=["GET"]
)(MovimientoController.ver_demo_detalle)

# =========================================
# ULTIMOS ESTATUS
# =========================================

movimiento_routes.route(
    "/api/ultimos_estatus",
    methods=["GET"]
)(
    MovimientoController.ultimos_estatus
)